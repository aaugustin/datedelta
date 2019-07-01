import datetime


class datedelta:

    __slots__ = ['_years', '_months', '_days']

    def __init__(self, *, years=0, months=0, days=0):
        int_years = int(years)
        int_months = int(months)
        int_days = int(days)

        if int_years != years:
            raise ValueError("years must be an integer value")
        if int_months != months:
            raise ValueError("months must be an integer value")
        if int_days != days:
            raise ValueError("days must be an integer value")

        self._years = int_years
        self._months = int_months
        self._days = int_days

    # datedelta must be immutable to be hashable.

    @property
    def years(self):
        return self._years

    @property
    def months(self):
        return self._months

    @property
    def days(self):
        return self._days

    def __repr__(self):
        args = []
        if self._years != 0:
            args.append('years={}'.format(self._years))
        if self._months != 0:
            args.append('months={}'.format(self._months))
        if self._days != 0:
            args.append('days={}'.format(self._days))
        return 'datedelta.datedelta({})'.format(', '.join(args))

    def __str__(self):
        bits = []
        if self._years != 0:
            bits.append('{} year{}'.format(self._years, _s(self._years)))
        if self._months != 0:
            bits.append('{} month{}'.format(self._months, _s(self._months)))
        if self._days != 0:
            bits.append('{} day{}'.format(self._days, _s(self._days)))
        return ', '.join(bits) or '0 days'

    def __eq__(self, other):
        if isinstance(other, datedelta):
            return (self._years == other._years and
                    self._months == other._months and
                    self._days == other._days)

        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, datedelta):
            return (self._years != other._years or
                    self._months != other._months or
                    self._days != other._days)

        return NotImplemented

    def __hash__(self):
        return hash((self._years, self._months, self._days))

    def __add__(self, other):
        if isinstance(other, datedelta):
            if (
                self._years * other._years >= 0 and
                self._months * other._months >= 0 and
                self._days * other._days >= 0
            ):
                return self.__class__(
                    years=self._years + other._years,
                    months=self._months + other._months,
                    days=self._days + other._days,
                )
            else:
                raise ValueError("cannot add datedeltas with opposite signs")

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, datedelta):
            if (
                self._years * other._years <= 0 and
                self._months * other._months <= 0 and
                self._days * other._days <= 0
            ):
                return self.__class__(
                    years=self._years - other._years,
                    months=self._months - other._months,
                    days=self._days - other._days,
                )
            else:
                raise ValueError("cannot subtract datedeltas with same signs")

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(
                years=self._years * other,
                months=self._months * other,
                days=self._days * other,
            )

        return NotImplemented

    def __radd__(self, other):
        # This also matches subclasseses such as datetime.datetime. We leave it
        # up to users to figure out whether that makes sense in their use case.
        if isinstance(other, datetime.date):
            year = other.year
            month = other.month
            day = other.day

            # Add years.
            if self._years:
                year += self._years
                # Adjust the month and day if the target day doesn't exist.
                if day > _days_in_month(year, month):
                    # This branch is never taken when month == 12 because day is
                    # always in 1..31 and because December has 31 days.
                    month += 1
                    day = 1

            # Add months.
            if self._months:
                month += self._months
                # Adjust the year if the target month isn't in 1..12.
                dyear, month0 = divmod(month - 1, 12)
                year += dyear
                month = month0 + 1
                # Adjust the month and day if the target day doesn't exist.
                if day > _days_in_month(year, month):
                    # This branch is never taken when month == 12 because day is
                    # always in 1..31 and because December has 31 days.
                    month += 1
                    day = 1

            result = other.replace(year, month, day)

            # Add days.
            if self._days:
                result += datetime.timedelta(days=self._days)

            return result

        return NotImplemented

    def __rsub__(self, other):
        # This also matches subclasseses such as datetime.datetime. We leave it
        # up to users to figure out whether that makes sense in their use case.
        if isinstance(other, datetime.date):
            year = other.year
            month = other.month
            day = other.day

            # Subtract years.
            if self._years:
                year -= self._years
                # Adjust the month and day if the target day doesn't exist.
                if day > _days_in_month(year, month):
                    # This branch is never taken when month == 12 because day is
                    # always in 1..31 and because December has 31 days.
                    month += 1
                    day = 1

            # Subtract months.
            if self._months:
                month -= self._months
                # Adjust the year if the target month isn't in 1..12.
                dyear, month0 = divmod(month - 1, 12)
                year += dyear
                month = month0 + 1
                # Adjust the month and day if the target day doesn't exist.
                if day > _days_in_month(year, month):
                    # This branch is never taken when month == 12 because day is
                    # always in 1..31 and because December has 31 days.
                    month += 1
                    day = 1

            result = other.replace(year, month, day)

            # Subtract days.
            if self._days:
                result -= datetime.timedelta(days=self._days)

            return result

        return NotImplemented

    __rmul__ = __mul__

    def __neg__(self):
        return self.__class__(
            years=-self._years,
            months=-self._months,
            days=-self._days,
        )

    def __pos__(self):
        return self

    # Optimize pickling.

    def __getstate__(self):
        return self._years, self._months, self._days

    def __setstate__(self, state):
        self._years, self._months, self._days = state


# Public constants for convenience.

YEAR = datedelta(years=1)

MONTH = datedelta(months=1)

WEEK = datedelta(days=7)

DAY = datedelta(days=1)


# There's a private implementation of the same logic in the datetime module.

_DAYS_IN_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _days_in_month(year, month):
    assert 1 <= month <= 12

    # Inline definition of calendar.isleap(year) for clarity and performance.
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return 29
    return _DAYS_IN_MONTH[month]


def _s(value):
    return '' if abs(value) == 1 else 's'
