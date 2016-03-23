datedelta
#########

``datedelta.datedelta`` is ``datetime.timedelta`` for date arithmetic.

It can add years, months, or days to dates while accounting for oddities of the
Gregorian calendar. It can also subtract years, months, or days from dates.

Typically, it's useful to compute yearly or monthly subscriptions periods.

Behavior
========

There are two date arithmetic traps in the Gregorian calendar:

1. Leap years. Problems arise when adding years to a February 29th gives a
   result in a non-leap year.

2. Variable number of days in months. Problems arise when adding months to a
   29th, 30th or 31st gives a result in a month where that day doesn't exist.

In both cases, the result must be changed to the first day of the next month.

Provided periods are represented by [start date inclusive, end date exclusive),
datedelta gives consistent results. (This representation of periods is akin to
0-based indexing, which is the convention Python uses.)

Operations are always performed on years, then months, then days. This order
usually provides the expected behavior. It also minimizes loss of precision.

Limitations
===========

Additions involving ``datedelta`` are neither associative not commutative in
general. Here are two examples where adding a ``datedelta`` then subtracting it
doesn't return the original value::

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2020, 2, 29) + datedelta.datedelta(years=1)
    datetime.date(2021, 3, 1)

    >>> datetime.date(2021, 3, 1) - datedelta.datedelta(years=1)
    datetime.date(2020, 3, 1)

    >>> datetime.date(2020, 1, 31) + datedelta.datedelta(months=1)
    datetime.date(2020, 3, 1)

    >>> datetime.date(2020, 3, 1) - datedelta.datedelta(months=1)
    datetime.date(2020, 2, 1)

To avoid counter-intuitive results, ``datedelta`` only implements operations
that have unambiguous semantics:

* Adding a datedelta to a date
* Subtracting a datedelta from a date
* Adding a datedelta to a datedelta when components have the same sign
* Subtracting a datedelta from a datedelta when components have opposite signs

(PEP 20 says: "In the face of ambiguity, refuse the temptation to guess.")

Alternatives
============

``datedelta.datedelta`` is smarter than ``datetime.timedelta`` because it knows
about years and months in addition to days.

``datedelta.datedelta`` provides a subset of the features found in
``dateutil.relativedelta``. Not only does it only support dates, but:

* It omits the "replace" behavior which is very error-prone.
* It doesn't allow explicit control of leapdays.
* It uses keyword-only arguments.
* It requires Python 3.

Handling leap days automatically reduces the number of choices the programmer
must make and thus the number of errors they can make.

If you're stuck with Python 2, just copy the code, make ``datedelta`` inherit
from ``object``, and remove the ``*`` in the signature of ``__init__``.

If you're comfortable with ``dateutil`` and don't mind its larger footprint,
there's little to gain by switching to ``datedelta``.

Changelog
=========

1.0
---

* Initial stable release.
