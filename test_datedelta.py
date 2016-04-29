# For convenience and readability in tests, use short aliases.

from datetime import date as d
from datetime import timedelta as td

import pytest
from datedelta import datedelta as dd
from datedelta import DAY, MONTH, YEAR


@pytest.mark.parametrize(
    ('constant', 'value'),
    [
        (DAY, dd(days=1)),
        (MONTH, dd(months=1)),
        (YEAR, dd(years=1)),
    ],
)
def test_constants(constant, value):
    assert constant == value


def test_years_must_be_integer():
    with pytest.raises(ValueError) as exc:
        dd(years=4.5)

    assert "years must be an integer value" in str(exc)


def test_months_must_be_integer():
    with pytest.raises(ValueError) as exc:
        dd(months=6.5)

    assert "months must be an integer value" in str(exc)


def test_weeks_must_be_integer():
    with pytest.raises(ValueError) as exc:
        dd(weeks=7.5)

    assert "weeks must be an integer value" in str(exc)


def test_days_must_be_integer():
    with pytest.raises(ValueError) as exc:
        dd(days=8.5)

    assert "days must be an integer value" in str(exc)


def test_can_get_years_attribute():
    assert dd(years=2, months=3, weeks=4, days=6).years == 2


def test_can_get_months_attribute():
    assert dd(years=2, months=3, weeks=4, days=6).months == 3


def test_can_get_weeks_attribute():
    assert dd(years=2, months=3, weeks=4, days=6).weeks == 4


def test_can_get_days_attribute():
    assert dd(years=2, months=3, weeks=4, days=6).days == 6


def test_cannot_set_years_attribute():
    delta = dd(years=2, months=3, weeks=4, days=6)
    with pytest.raises(AttributeError):
        delta.years = 2


def test_cannot_set_months_attribute():
    delta = dd(years=2, months=3, weeks=4, days=6)
    with pytest.raises(AttributeError):
        delta.years = 3


def test_cannot_set_days_attribute():
    delta = dd(years=2, months=3, weeks=4, days=6)
    with pytest.raises(AttributeError):
        delta.years = 6


def test_cannot_delete_years_attribute():
    delta = dd(years=2, months=3, weeks=4, days=6)
    with pytest.raises(AttributeError):
        del delta.years


def test_cannot_delete_months_attribute():
    delta = dd(years=2, months=3, weeks=4, days=6)
    with pytest.raises(AttributeError):
        del delta.years


def test_cannot_delete_days_attribute():
    delta = dd(years=2, months=3, weeks=4, days=6)
    with pytest.raises(AttributeError):
        del delta.years


@pytest.mark.parametrize(
    ('delta_repr', 'delta_str'),
    [
        # No values.
        ('dd()', '0 days'),
        # Positive singular values.
        ('dd(years=1)', '1 year'),
        ('dd(months=1)', '1 month'),
        ('dd(weeks=1)', '1 week'),
        ('dd(days=1)', '1 day'),
        ('dd(years=1, months=1)', '1 year, 1 month'),
        ('dd(years=1, weeks=1)', '1 year, 1 week'),
        ('dd(years=1, days=1)', '1 year, 1 day'),
        ('dd(months=1, weeks=1)', '1 month, 1 week'),
        ('dd(months=1, days=1)', '1 month, 1 day'),
        ('dd(weeks=1, days=1)', '1 week, 1 day'),
        ('dd(years=1, months=1, weeks=1, days=1)', '1 year, 1 month, 1 week, 1 day'),
        # Negative singular values.
        ('dd(years=-1)', '-1 year'),
        ('dd(months=-1)', '-1 month'),
        ('dd(weeks=-1)', '-1 week'),
        ('dd(days=-1)', '-1 day'),
        ('dd(years=-1, months=-1)', '-1 year, -1 month'),
        ('dd(years=-1, weeks=-1)', '-1 year, -1 week'),
        ('dd(years=-1, days=-1)', '-1 year, -1 day'),
        ('dd(months=-1, weeks=-1)', '-1 month, -1 week'),
        ('dd(months=-1, days=-1)', '-1 month, -1 day'),
        ('dd(weeks=-1, days=-1)', '-1 week, -1 day'),
        ('dd(years=-1, months=-1, weeks=-1, days=-1)', '-1 year, -1 month, -1 week, -1 day'),
        # Mixed singular values.
        ('dd(years=1, months=-1)', '1 year, -1 month'),
        ('dd(years=-1, months=1)', '-1 year, 1 month'),
        ('dd(years=1, weeks=-1)', '1 year, -1 week'),
        ('dd(years=-1, weeks=1)', '-1 year, 1 week'),
        ('dd(years=1, days=-1)', '1 year, -1 day'),
        ('dd(years=-1, days=1)', '-1 year, 1 day'),
        ('dd(months=1, weeks=-1)', '1 month, -1 week'),
        ('dd(months=-1, weeks=1)', '-1 month, 1 week'),
        ('dd(months=1, days=-1)', '1 month, -1 day'),
        ('dd(months=-1, days=1)', '-1 month, 1 day'),
        ('dd(weeks=1, days=-1)', '1 week, -1 day'),
        ('dd(weeks=-1, days=1)', '-1 week, 1 day'),
        ('dd(years=1, months=1, weeks=1, days=-1)', '1 year, 1 month, 1 week, -1 day'),
        ('dd(years=1, months=1, weeks=-1, days=1)', '1 year, 1 month, -1 week, 1 day'),
        ('dd(years=1, months=1, weeks=-1, days=-1)', '1 year, 1 month, -1 week, -1 day'),
        ('dd(years=1, months=-1, weeks=1, days=1)', '1 year, -1 month, 1 week, 1 day'),
        ('dd(years=1, months=-1, weeks=1, days=-1)', '1 year, -1 month, 1 week, -1 day'),
        ('dd(years=1, months=-1, weeks=-1, days=1)', '1 year, -1 month, -1 week, 1 day'),
        ('dd(years=1, months=-1, weeks=-1, days=-1)', '1 year, -1 month, -1 week, -1 day'),
        ('dd(years=-1, months=1, weeks=1, days=1)', '-1 year, 1 month, 1 week, 1 day'),
        ('dd(years=-1, months=1, weeks=1, days=-1)', '-1 year, 1 month, 1 week, -1 day'),
        ('dd(years=-1, months=1, weeks=-1, days=1)', '-1 year, 1 month, -1 week, 1 day'),
        ('dd(years=-1, months=1, weeks=-1, days=-1)', '-1 year, 1 month, -1 week, -1 day'),
        ('dd(years=-1, months=-1, weeks=1, days=1)', '-1 year, -1 month, 1 week, 1 day'),
        ('dd(years=-1, months=-1, weeks=1, days=-1)', '-1 year, -1 month, 1 week, -1 day'),
        ('dd(years=-1, months=-1, weeks=-1, days=1)', '-1 year, -1 month, -1 week, 1 day'),
        # Positive plural values.
        ('dd(years=2)', '2 years'),
        ('dd(months=3)', '3 months'),
        ('dd(weeks=4)', '4 weeks'),
        ('dd(days=6)', '6 days'),
        ('dd(years=2, months=3)', '2 years, 3 months'),
        ('dd(years=2, weeks=4)', '2 years, 4 weeks'),
        ('dd(years=2, days=6)', '2 years, 6 days'),
        ('dd(months=3, weeks=4)', '3 months, 4 weeks'),
        ('dd(months=3, days=6)', '3 months, 6 days'),
        ('dd(weeks=4, days=6)', '4 weeks, 6 days'),
        ('dd(years=2, months=3, weeks=4, days=6)', '2 years, 3 months, 4 weeks, 6 days'),
        # Negative plural values.
        ('dd(years=-2)', '-2 years'),
        ('dd(months=-3)', '-3 months'),
        ('dd(weeks=-4)', '-4 weeks'),
        ('dd(days=-6)', '-6 days'),
        ('dd(years=-2, months=-3)', '-2 years, -3 months'),
        ('dd(years=-2, weeks=-4)', '-2 years, -4 weeks'),
        ('dd(years=-2, days=-6)', '-2 years, -6 days'),
        ('dd(months=-3, weeks=-4)', '-3 months, -4 weeks'),
        ('dd(months=-3, days=-6)', '-3 months, -6 days'),
        ('dd(weeks=-4, days=-6)', '-4 weeks, -6 days'),
        ('dd(years=-2, months=-3, weeks=-4, days=-6)', '-2 years, -3 months, -4 weeks, -6 days'),
        # Mixed plural values.
        ('dd(years=2, months=-3)', '2 years, -3 months'),
        ('dd(years=-2, months=3)', '-2 years, 3 months'),
        ('dd(years=2, weeks=-4)', '2 years, -4 weeks'),
        ('dd(years=-2, weeks=4)', '-2 years, 4 weeks'),
        ('dd(years=2, days=-6)', '2 years, -6 days'),
        ('dd(years=-2, days=6)', '-2 years, 6 days'),
        ('dd(months=3, weeks=-4)', '3 months, -4 weeks'),
        ('dd(months=-3, weeks=4)', '-3 months, 4 weeks'),
        ('dd(months=3, days=-6)', '3 months, -6 days'),
        ('dd(months=-3, days=6)', '-3 months, 6 days'),
        ('dd(weeks=4, days=-6)', '4 weeks, -6 days'),
        ('dd(weeks=-4, days=6)', '-4 weeks, 6 days'),
        ('dd(years=2, months=3, weeks=4, days=-6)', '2 years, 3 months, 4 weeks, -6 days'),
        ('dd(years=2, months=3, weeks=-4, days=6)', '2 years, 3 months, -4 weeks, 6 days'),
        ('dd(years=2, months=3, weeks=-4, days=-6)', '2 years, 3 months, -4 weeks, -6 days'),
        ('dd(years=2, months=-3, weeks=4, days=6)', '2 years, -3 months, 4 weeks, 6 days'),
        ('dd(years=2, months=-3, weeks=4, days=-6)', '2 years, -3 months, 4 weeks, -6 days'),
        ('dd(years=2, months=-3, weeks=-4, days=6)', '2 years, -3 months, -4 weeks, 6 days'),
        ('dd(years=2, months=-3, weeks=-4, days=-6)', '2 years, -3 months, -4 weeks, -6 days'),
        ('dd(years=-2, months=3, weeks=4, days=6)', '-2 years, 3 months, 4 weeks, 6 days'),
        ('dd(years=-2, months=3, weeks=4, days=-6)', '-2 years, 3 months, 4 weeks, -6 days'),
        ('dd(years=-2, months=3, weeks=-4, days=6)', '-2 years, 3 months, -4 weeks, 6 days'),
        ('dd(years=-2, months=3, weeks=-4, days=-6)', '-2 years, 3 months, -4 weeks, -6 days'),
        ('dd(years=-2, months=-3, weeks=4, days=6)', '-2 years, -3 months, 4 weeks, 6 days'),
        ('dd(years=-2, months=-3, weeks=4, days=-6)', '-2 years, -3 months, 4 weeks, -6 days'),
        ('dd(years=-2, months=-3, weeks=-4, days=6)', '-2 years, -3 months, -4 weeks, 6 days'),
        # Mixed singular and plural values (not all combinations are included).
        ('dd(years=-1, months=1, days=10)', '-1 year, 1 month, 10 days'),
        ('dd(months=2, days=-1)', '2 months, -1 day'),
        ('dd(months=-1, days=10)', '-1 month, 10 days'),
        ('dd(weeks=3, days=-1)', '3 weeks, -1 day'),
        ('dd(years=1, weeks=-4)', '1 year, -4 weeks'),
    ],
)
def test_repr_and_str(delta_repr, delta_str):
    delta = eval(delta_repr)            # repr must be evaluable
    delta_repr = delta_repr.replace('dd', 'datedelta.datedelta')
    assert repr(delta) == delta_repr    # repr must round-trip (on test cases)
    assert str(delta) == delta_str


@pytest.mark.parametrize(
    ('delta_1', 'delta_2', 'is_equal'),
    [
        # Same type.
        (dd(), dd(), True),
        (dd(), dd(years=0, months=0, weeks=0, days=0), True),
        (dd(years=2), dd(years=2), True),
        (dd(years=2), dd(years=2, months=0, weeks=0, days=0), True),
        (dd(months=3, weeks=4), dd(months=3, weeks=4), True),
        (dd(months=3, weeks=4, days=0), dd(years=0, months=3, weeks=4), True),
        (dd(months=3, days=6), dd(months=3, days=6), True),
        (dd(months=3, days=6), dd(years=0, months=3, days=6), True),
        (dd(years=2, months=3, weeks=4, days=6), dd(years=2, months=3, weeks=4, days=6), True),
        (dd(), dd(years=2), False),
        (dd(years=1), dd(years=2), False),
        (dd(), dd(months=3, days=6), False),
        (dd(months=3, days=6), dd(months=3, days=3), False),
        (dd(), dd(weeks=2), False),
        (dd(weeks=1), dd(weeks=2), False),
        (dd(years=2), dd(months=3, days=6), False),
        (dd(years=2), dd(years=2, months=3, weeks=4, days=6), False),
        # Other types.
        (dd(), 0, False),
        (dd(), None, False),
        (dd(), True, False),
        (dd(), False, False),
        (dd(years=2, months=3, days=6), d(year=2, month=3, day=6), False),
        (dd(days=6), td(days=6), False),
    ],
)
def test_equal_not_equal_and_hash(delta_1, delta_2, is_equal):
    assert (delta_1 == delta_2) == is_equal
    assert (delta_2 == delta_1) == is_equal
    assert (delta_1 != delta_2) != is_equal
    assert (delta_2 != delta_1) != is_equal
    if type(delta_1) == type(delta_2) == dd:
        # Technically, hashes could be equal even if values are different, but
        # that case doesn't happen in the current implementation.
        assert (hash(delta_1) == hash(delta_2)) == is_equal


@pytest.mark.parametrize(
    ('delta_1', 'delta_2', 'delta'),
    [
        (dd(), dd(), dd()),
        # Positive deltas.
        (dd(years=2), dd(), dd(years=2)),
        (dd(), dd(months=3, days=6), dd(months=3, days=6)),
        (dd(), dd(months=3, weeks=4), dd(months=3, weeks=4)),
        (dd(years=1), dd(years=1), dd(years=2)),
        (dd(years=2), dd(months=3, days=6), dd(years=2, months=3, days=6)),
        (dd(years=2), dd(weeks=4, days=6), dd(years=2, weeks=4, days=6)),
        (dd(years=2, months=1), dd(months=2, days=6), dd(years=2, months=3, days=6)),
        (dd(years=2, months=1, days=2), dd(months=2, days=4), dd(years=2, months=3, days=6)),
        (dd(years=2, months=1, weeks=1, days=2), dd(months=2, days=4), dd(years=2, months=3, weeks=1, days=6)),
        # Negative deltas.
        (dd(years=-2), dd(), dd(years=-2)),
        (dd(), dd(months=-3, days=-6), dd(months=-3, days=-6)),
        (dd(), dd(months=-3, weeks=-4), dd(months=-3, weeks=-4)),
        (dd(years=-1), dd(years=-1), dd(years=-2)),
        (dd(years=-2), dd(months=-3, days=-6), dd(years=-2, months=-3, days=-6)),
        (dd(years=-2), dd(weeks=-4, days=-6), dd(years=-2, weeks=-4, days=-6)),
        (dd(years=-2, months=-1), dd(months=-2, days=-6), dd(years=-2, months=-3, days=-6)),
        (dd(years=-2, months=-1, days=-2), dd(months=-2, days=-4), dd(years=-2, months=-3, days=-6)),
        (dd(years=-2, months=-1, weeks=-1, days=-2), dd(months=-2, days=-4), dd(years=-2, months=-3, weeks=-1, days=-6)),
        # Supported mixed deltas.
        (dd(years=2), dd(months=-3, days=6), dd(years=2, months=-3, days=6)),
        (dd(years=2), dd(weeks=-4, days=6), dd(years=2, weeks=-4, days=6)),
        (dd(years=-2, months=1), dd(months=2, days=-6), dd(years=-2, months=3, days=-6)),
        (dd(years=2, months=1, days=-2), dd(months=2, days=-4), dd(years=2, months=3, days=-6)),
        (dd(years=2, months=-1, weeks=1, days=-2), dd(months=-2, weeks=2, days=-4), dd(years=2, months=-3, weeks=3, days=-6)),
    ]
)
def test_add_datedelta(delta_1, delta_2, delta):
    assert delta_1 + delta_2 == delta


@pytest.mark.parametrize(
    ('delta_1', 'delta_2'),
    [
        # Unsupported mixed deltas.
        (dd(years=3), dd(years=-1)),
        (dd(years=2, months=5), dd(months=-2, days=-6)),
        (dd(years=2, months=1, days=-10), dd(months=2, days=4)),
    ]
)
def test_add_unsupported_datedelta(delta_1, delta_2):
    with pytest.raises(ValueError) as exc:
        delta_1 + delta_2
    assert "cannot add datedeltas with opposite signs" in str(exc)


@pytest.mark.parametrize(
    ('delta_1', 'other'),
    [
        # Other types.
        (dd(), None),
        (dd(), 0),
        (dd(), 'a'),
        (dd(), []),
        (dd(), d.today()),
    ]
)
def test_add_unsupported_type(delta_1, other):
    with pytest.raises(TypeError) as exc:
        delta_1 + other
    assert "unsupported operand type(s) for +" in str(exc)


@pytest.mark.parametrize(
    ('delta_1', 'delta_2', 'delta'),
    [
        (dd(), dd(), dd()),
        # Positive deltas.
        (dd(years=2), dd(), dd(years=2)),
        (dd(), dd(months=-3, days=-6), dd(months=3, days=6)),
        (dd(years=1), dd(years=-1), dd(years=2)),
        (dd(years=2), dd(months=-3, days=-6), dd(years=2, months=3, days=6)),
        (dd(years=2, months=1), dd(months=-2, days=-6), dd(years=2, months=3, days=6)),
        (dd(years=2, months=1, days=2), dd(months=-2, days=-4), dd(years=2, months=3, days=6)),
        # Negative deltas.
        (dd(years=-2), dd(), dd(years=-2)),
        (dd(), dd(months=3, days=6), dd(months=-3, days=-6)),
        (dd(years=-1), dd(years=1), dd(years=-2)),
        (dd(years=-2), dd(months=3, days=6), dd(years=-2, months=-3, days=-6)),
        (dd(years=-2, months=-1), dd(months=2, days=6), dd(years=-2, months=-3, days=-6)),
        (dd(years=-2, months=-1, days=-2), dd(months=2, days=4), dd(years=-2, months=-3, days=-6)),
        # Supported mixed deltas.
        (dd(years=2), dd(months=3, days=-6), dd(years=2, months=-3, days=6)),
        (dd(years=-2, months=1), dd(months=-2, days=6), dd(years=-2, months=3, days=-6)),
        (dd(years=2, months=1, days=-2), dd(months=-2, days=4), dd(years=2, months=3, days=-6)),
    ]
)
def test_subtract_datedelta(delta_1, delta_2, delta):
    assert delta_1 - delta_2 == delta


@pytest.mark.parametrize(
    ('delta_1', 'delta_2'),
    [
        # Unsupported mixed deltas.
        (dd(years=3), dd(years=1)),
        (dd(years=2, months=5), dd(months=2, days=6)),
        (dd(years=2, months=1, days=-10), dd(months=-2, days=-4)),
    ]
)
def test_subtract_unsupported_datedelta(delta_1, delta_2):
    with pytest.raises(ValueError) as exc:
        delta_1 - delta_2
    assert "cannot subtract datedeltas with same signs" in str(exc)


@pytest.mark.parametrize(
    ('delta_1', 'count', 'delta'),
    [
        (dd(), 0, dd()),
        (dd(), 1, dd()),
        (dd(), 2, dd()),
        (dd(), -1, dd()),
        (dd(years=1), 0, dd()),
        (dd(years=1), 1, dd(years=1)),
        (dd(years=1), 2, dd(years=2)),
        (dd(years=1), -1, dd(years=-1)),
        (dd(years=2, months=3, days=6), 0, dd()),
        (dd(years=2, months=3, days=6), 1, dd(years=2, months=3, days=6)),
        (dd(years=2, months=3, days=6), 2, dd(years=4, months=6, days=12)),
        (dd(years=2, months=3, days=6), -1, dd(years=-2, months=-3, days=-6)),
    ]
)
def test_multiply_integer(delta_1, count, delta):
    assert delta_1 * count == delta
    assert count * delta_1 == delta


@pytest.mark.parametrize(
    ('date_1', 'delta', 'date_2'),
    [
        (d(2020, 1, 1), dd(), d(2020, 1, 1)),
        (d(2020, 2, 29), dd(), d(2020, 2, 29)),
        (d(2020, 3, 1), dd(), d(2020, 3, 1)),
        (d(2020, 12, 31), dd(), d(2020, 12, 31)),
        (d(2020, 1, 1), dd(years=1), d(2021, 1, 1)),
        (d(2020, 2, 29), dd(years=1), d(2021, 3, 1)),
        (d(2020, 3, 1), dd(years=1), d(2021, 3, 1)),
        (d(2020, 12, 31), dd(years=1), d(2021, 12, 31)),
        (d(2020, 1, 1), dd(months=12), d(2021, 1, 1)),
        (d(2020, 2, 29), dd(months=12), d(2021, 3, 1)),
        (d(2020, 3, 1), dd(months=12), d(2021, 3, 1)),
        (d(2020, 12, 31), dd(months=12), d(2021, 12, 31)),
        (d(2020, 1, 1), dd(days=365), d(2020, 12, 31)),
        (d(2020, 2, 29), dd(days=365), d(2021, 2, 28)),
        (d(2020, 3, 1), dd(days=365), d(2021, 3, 1)),
        (d(2020, 12, 31), dd(days=365), d(2021, 12, 31)),
        (d(2020, 1, 1), dd(years=1, days=-10), d(2020, 12, 22)),
        (d(2020, 2, 29), dd(years=1, days=-10), d(2021, 2, 19)),
        (d(2020, 3, 1), dd(years=1, days=-10), d(2021, 2, 19)),
        (d(2020, 12, 31), dd(years=1, days=-10), d(2021, 12, 21)),
        (d(2021, 1, 1), dd(years=-1), d(2020, 1, 1)),
        (d(2021, 2, 28), dd(years=-1), d(2020, 2, 28)),
        (d(2021, 3, 1), dd(years=-1), d(2020, 3, 1)),
        (d(2021, 12, 31), dd(years=-1), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(months=-12), d(2020, 1, 1)),
        (d(2021, 2, 28), dd(months=-12), d(2020, 2, 28)),
        (d(2021, 3, 1), dd(months=-12), d(2020, 3, 1)),
        (d(2021, 12, 31), dd(months=-12), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(days=-365), d(2020, 1, 2)),
        (d(2021, 2, 28), dd(days=-365), d(2020, 2, 29)),
        (d(2021, 3, 1), dd(days=-365), d(2020, 3, 1)),
        (d(2021, 12, 31), dd(days=-365), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(years=-1, days=10), d(2020, 1, 11)),
        (d(2021, 2, 28), dd(years=-1, days=10), d(2020, 3, 9)),
        (d(2021, 3, 1), dd(years=-1, days=10), d(2020, 3, 11)),
        (d(2021, 12, 31), dd(years=-1, days=10), d(2021, 1, 10)),
    ]
)
def test_add_datedelta_to_date(date_1, delta, date_2):
    assert date_1 + delta == date_2


@pytest.mark.parametrize(
    ('date_1', 'delta', 'date_2'),
    [
        (d(2020, 1, 1), dd(), d(2020, 1, 1)),
        (d(2020, 2, 29), dd(), d(2020, 2, 29)),
        (d(2020, 3, 1), dd(), d(2020, 3, 1)),
        (d(2020, 12, 31), dd(), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(years=1), d(2020, 1, 1)),
        (d(2021, 2, 28), dd(years=1), d(2020, 2, 28)),
        (d(2021, 3, 1), dd(years=1), d(2020, 3, 1)),
        (d(2021, 12, 31), dd(years=1), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(months=12), d(2020, 1, 1)),
        (d(2021, 2, 28), dd(months=12), d(2020, 2, 28)),
        (d(2021, 3, 1), dd(months=12), d(2020, 3, 1)),
        (d(2021, 12, 31), dd(months=12), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(days=365), d(2020, 1, 2)),
        (d(2021, 2, 28), dd(days=365), d(2020, 2, 29)),
        (d(2021, 3, 1), dd(days=365), d(2020, 3, 1)),
        (d(2021, 12, 31), dd(days=365), d(2020, 12, 31)),
        (d(2021, 1, 1), dd(years=1, days=-10), d(2020, 1, 11)),
        (d(2021, 2, 28), dd(years=1, days=-10), d(2020, 3, 9)),
        (d(2021, 3, 1), dd(years=1, days=-10), d(2020, 3, 11)),
        (d(2021, 12, 31), dd(years=1, days=-10), d(2021, 1, 10)),
        (d(2020, 1, 1), dd(years=-1), d(2021, 1, 1)),
        (d(2020, 2, 29), dd(years=-1), d(2021, 3, 1)),
        (d(2020, 3, 1), dd(years=-1), d(2021, 3, 1)),
        (d(2020, 12, 31), dd(years=-1), d(2021, 12, 31)),
        (d(2020, 1, 1), dd(months=-12), d(2021, 1, 1)),
        (d(2020, 2, 29), dd(months=-12), d(2021, 3, 1)),
        (d(2020, 3, 1), dd(months=-12), d(2021, 3, 1)),
        (d(2020, 12, 31), dd(months=-12), d(2021, 12, 31)),
        (d(2020, 1, 1), dd(days=-365), d(2020, 12, 31)),
        (d(2020, 2, 29), dd(days=-365), d(2021, 2, 28)),
        (d(2020, 3, 1), dd(days=-365), d(2021, 3, 1)),
        (d(2020, 12, 31), dd(days=-365), d(2021, 12, 31)),
        (d(2020, 1, 1), dd(years=-1, days=10), d(2020, 12, 22)),
        (d(2020, 2, 29), dd(years=-1, days=10), d(2021, 2, 19)),
        (d(2020, 3, 1), dd(years=-1, days=10), d(2021, 2, 19)),
        (d(2020, 12, 31), dd(years=-1, days=10), d(2021, 12, 21)),
    ]
)
def test_subtract_datedelta_from_date(date_1, delta, date_2):
    assert date_1 - delta == date_2


@pytest.mark.parametrize(
    ('delta', 'minus_delta'),
    [
        (dd(), dd()),
        (dd(years=2), dd(years=-2)),
        (dd(months=3, days=6), dd(months=-3, days=-6)),
        (dd(years=2, months=3, days=6), dd(years=-2, months=-3, days=-6)),
        (dd(years=-2), dd(years=2)),
        (dd(months=-3, days=-6), dd(months=3, days=6)),
        (dd(years=-2, months=-3, days=-6), dd(years=2, months=3, days=6)),
        (dd(years=2, months=-3, days=6), dd(years=-2, months=3, days=-6)),
    ]
)
def test_minus_datedelta(delta, minus_delta):
    assert -delta == minus_delta


@pytest.mark.parametrize(
    'delta',
    [
        dd(),
        dd(years=2),
        dd(months=3, days=6),
        dd(years=2, months=3, days=6),
        dd(years=-2),
        dd(months=-3, days=-6),
        dd(years=-2, months=-3, days=-6),
        dd(years=2, months=-3, days=6),
    ]
)
def test_plus_datedelta(delta):
    assert +delta == delta


@pytest.mark.parametrize(
    ('delta', 'other'),
    [
        (dd(), None),
        (dd(), 0),
        (dd(), 'a'),
        (dd(), []),
        (dd(), d.today()),
    ]
)
def test_add_or_subtract_unsupported_type(delta, other):
    with pytest.raises(TypeError):
        delta + other
    with pytest.raises(TypeError):
        delta - other


@pytest.mark.parametrize(
    ('delta', 'other'),
    [
        (dd(), None),
        (dd(), 0),
        (dd(), 'a'),
        (dd(), []),
    ]
)
def test_add_to_or_subtract_from_unsupported_type(delta, other):
    with pytest.raises(TypeError):
        other + delta
    with pytest.raises(TypeError):
        other - delta


@pytest.mark.parametrize(
    ('delta', 'other'),
    [
        (dd(), None),
        (dd(), 'a'),
        (dd(), []),
        (dd(), dd()),
    ]
)
def test_multiply_unsupported_type(delta, other):
    with pytest.raises(TypeError):
        delta * other
    with pytest.raises(TypeError):
        other * delta
