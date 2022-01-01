datedelta
#########

``datedelta.datedelta`` is ``datetime.timedelta`` for date arithmetic.

.. code-block:: pycon

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2025, 4, 22) + 2 * datedelta.WEEK
    datetime.date(2025, 5, 6)

    >>> datetime.date(2025, 4, 22) + 3 * datedelta.MONTH
    datetime.date(2025, 7, 22)

It accounts for oddities of the Gregorian calendar.

.. code-block:: pycon

    >>> datetime.date(2024, 2, 29) + datedelta.YEAR
    datetime.date(2025, 3, 1)

    >>> datetime.date(2024, 2, 29) + 4 * datedelta.YEAR
    datetime.date(2028, 2, 29)

It's convenient for computing yearly, monthly, or weekly subscriptions periods.

.. code-block:: pycon

    >>> start_date = datetime.date(2024, 1, 30)
    >>> for n in range(12):
    ...     print(repr(start_date + n * datedelta.MONTH))
    datetime.date(2024, 1, 30)
    datetime.date(2024, 3, 1)
    datetime.date(2024, 3, 30)
    datetime.date(2024, 4, 30)
    datetime.date(2024, 5, 30)
    datetime.date(2024, 6, 30)
    datetime.date(2024, 7, 30)
    datetime.date(2024, 8, 30)
    datetime.date(2024, 9, 30)
    datetime.date(2024, 10, 30)
    datetime.date(2024, 11, 30)
    datetime.date(2024, 12, 30)

    >>> start_date = datetime.date(2024, 1, 31)
    >>> for n in range(12):
    ...     print(repr(start_date + n * datedelta.MONTH))
    datetime.date(2024, 1, 31)
    datetime.date(2024, 3, 1)
    datetime.date(2024, 3, 31)
    datetime.date(2024, 5, 1)
    datetime.date(2024, 5, 31)
    datetime.date(2024, 7, 1)
    datetime.date(2024, 7, 31)
    datetime.date(2024, 8, 31)
    datetime.date(2024, 10, 1)
    datetime.date(2024, 10, 31)
    datetime.date(2024, 12, 1)
    datetime.date(2024, 12, 31)

It guarantees consistent results on arithmetic operations that it supports.

Behavior
========

There are two date arithmetic traps in the Gregorian calendar:

1. Leap years. Problems arise when adding years to a February 29th gives a
   result in a non-leap year.

2. Variable number of days in months. Problems arise when adding months to a
   29th, 30th or 31st gives a result in a month where that day doesn't exist.

In both cases, datedelta changes the result to the first day of the next month.

This method gives consistent results provided periods are represented by
(start date inclusive, end date exclusive) — that's [start date, end date) if
you prefer the mathematical notation. This representation of periods is akin
to 0-based indexing, which is the convention Python uses.

For example:

* If someone subscribes for a year starting on 2020-02-29 inclusive, the end
  date must be 2021-03-01 exclusive. If it was 2020-02-28 exclusive, that day
  would be missing from the subscription period.

* If someone subscribes for three months starting on 2020-03-31 inclusive, the
  end date must be 2020-07-01 exclusive. If it was 2020-06-30 exclusive, that
  day would be missing from the subscription period.

Operations are always performed on years, then months, then days. This order
usually provides the expected behavior. It also minimizes loss of precision.

Installation
============

.. code-block:: bash

    pip install datedelta

Usage
=====

The most common operations are adding a ``datedelta`` to a ``date`` and
subtracting a ``datedelta`` from a ``date``.

Basic intervals
---------------

The ``YEAR``, ``MONTH``, ``WEEK``, and ``DAY`` constants support common
calculations with little code.

.. code-block:: pycon

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2022, 1, 1) + datedelta.YEAR
    datetime.date(2023, 1, 1)

    >>> datetime.date(2023, 1, 1) - datedelta.YEAR
    datetime.date(2022, 1, 1)

    >>> datetime.date(2024, 2, 29) + datedelta.YEAR
    datetime.date(2025, 3, 1)

    >>> datetime.date(2025, 3, 1) - datedelta.YEAR
    datetime.date(2024, 3, 1)

    >>> datetime.date(2022, 1, 1) + datedelta.MONTH
    datetime.date(2022, 2, 1)

    >>> datetime.date(2022, 2, 1) - datedelta.MONTH
    datetime.date(2022, 1, 1)

    >>> datetime.date(2022, 1, 31) + datedelta.MONTH
    datetime.date(2022, 3, 1)

    >>> datetime.date(2022, 3, 1) - datedelta.MONTH
    datetime.date(2022, 2, 1)

    >>> datetime.date(2022, 1, 1) + datedelta.WEEK
    datetime.date(2022, 1, 8)

    >>> datetime.date(2022, 1, 1) - datedelta.WEEK
    datetime.date(2021, 12, 25)

    >>> datetime.date(2022, 1, 1) + datedelta.DAY
    datetime.date(2022, 1, 2)

    >>> datetime.date(2022, 1, 1) - datedelta.DAY
    datetime.date(2021, 12, 31)

``datedelta.DAY`` behaves exactly like ``datetime.timedelta(1)``. It's only
provided for consistency.

Arbitrary intervals
-------------------

``datedelta`` objects provide support for arbitrary calculations.

.. code-block:: pycon

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2022, 3, 23) + datedelta.datedelta(years=1, months=1, days=-1)
    datetime.date(2023, 4, 22)

    >>> datetime.date(2022, 3, 23) - datedelta.datedelta(years=-1, months=-1, days=1)
    datetime.date(2023, 4, 22)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=2)
    datetime.date(2026, 3, 1)

    >>> datetime.date(2024, 2, 29) - datedelta.datedelta(years=2)
    datetime.date(2022, 3, 1)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=2, days=-1)
    datetime.date(2026, 2, 28)

    >>> datetime.date(2024, 2, 29) - datedelta.datedelta(years=2, days=1)
    datetime.date(2022, 2, 28)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=2, months=6)
    datetime.date(2026, 9, 1)

    >>> datetime.date(2024, 2, 29) - datedelta.datedelta(years=2, months=-6)
    datetime.date(2022, 9, 1)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=4)
    datetime.date(2028, 2, 29)

    >>> datetime.date(2024, 2, 29) - datedelta.datedelta(years=4)
    datetime.date(2020, 2, 29)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=4, days=1)
    datetime.date(2028, 3, 1)

    >>> datetime.date(2024, 2, 29) - datedelta.datedelta(years=4, days=-1)
    datetime.date(2020, 3, 1)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=4, months=6)
    datetime.date(2028, 8, 29)

    >>> datetime.date(2024, 2, 29) - datedelta.datedelta(years=4, months=-6)
    datetime.date(2020, 8, 29)

These results are mathematically consistent, as explained in "Behavior" above.

Other operations
----------------

``datedelta`` instances can be added, subtracted, and multiplied with an
integer. However, there are some restrictions on addition and subtraction.

Adding then subtracting a given datedelta to a date doesn't always return the
original date. In order to prevent bugs caused by this behavior, when the result
of adding or subtracting two ``datedelta`` isn't well defined, a ``ValueError``
is raised.

.. code-block:: pycon

    >>> import datedelta

    >>> datedelta.YEAR + datedelta.YEAR
    datedelta.datedelta(years=2)

    >>> 3 * datedelta.YEAR
    datedelta.datedelta(years=3)

    >>> datedelta.YEAR - datedelta.DAY
    datedelta.datedelta(years=1, days=-1)

    >>> datedelta.YEAR - datedelta.YEAR
    Traceback (most recent call last):
        ...
    ValueError: cannot subtract datedeltas with same signs

    >>> datedelta.datedelta(months=6) + datedelta.datedelta(months=-3)
    Traceback (most recent call last):
        ...
    ValueError: cannot add datedeltas with opposite signs

Limitations
===========

Additions involving ``datedelta`` are neither associative nor commutative in
general.

Here are two examples where adding a ``datedelta`` then subtracting it doesn't
return the original value:

.. code-block:: pycon

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=1)
    datetime.date(2025, 3, 1)

    >>> datetime.date(2025, 3, 1) - datedelta.datedelta(years=1)
    datetime.date(2024, 3, 1)

    >>> datetime.date(2024, 1, 31) + datedelta.datedelta(months=1)
    datetime.date(2024, 3, 1)

    >>> datetime.date(2024, 3, 1) - datedelta.datedelta(months=1)
    datetime.date(2024, 2, 1)

Here are two examples where adding two ``datedelta`` gives a different result
depending on the order of operations:

.. code-block:: pycon

    >>> import datetime
    >>> import datedelta

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(months=6) + datedelta.datedelta(years=1)
    datetime.date(2025, 8, 29)

    >>> datetime.date(2024, 2, 29) + datedelta.datedelta(years=1) + datedelta.datedelta(months=6)
    datetime.date(2025, 9, 1)

    >>> datetime.date(2024, 1, 31) + datedelta.datedelta(months=2) + datedelta.datedelta(months=5)
    datetime.date(2024, 8, 31)

    >>> datetime.date(2024, 1, 31) + datedelta.datedelta(months=5) + datedelta.datedelta(months=2)
    datetime.date(2024, 9, 1)

To avoid problems, you should always start from the same reference date and add
a single ``datedelta``. Don't chain additions or subtractions.

To minimize the risk of incorrect results, ``datedelta`` only implements
operations that have unambiguous semantics:

* Adding a datedelta to a date
* Subtracting a datedelta from a date
* Adding a datedelta to a datedelta when components have the same sign
* Subtracting a datedelta from a datedelta when components have opposite signs

(PEP 20 says: "In the face of ambiguity, refuse the temptation to guess.")

Alternatives
============

``datedelta.datedelta`` is smarter than ``datetime.timedelta`` because it knows
about years and months in addition to days.

Compared to ``pendulum.Duration`` or ``dateutil.relativedelta.relativedelta``,
``datedelta.datedelta`` has a few benefits:

* It handles non-existing results in a mathematically consistent fashion: it
  adjusts to the first day of the next month while pendulum and dateutil adjust
  to the last day of the current month.
* It provides an API designed to prevent programming mistakes: it requires
  keyword arguments, rejects operations expressing incorrect business logic, and
  omits error-prone features of dateutil like the "replace" behavior or explicit
  control of leap days.
* It has very small footprint, by virtue of providing of very small subset of
  the features found in pendulum or dateutil. That makes it a good choice if
  you're otherwise happy with the standard library's datetime module.

Changelog
=========

1.4
---

* Update supported Python versions.

1.3
---

* Add ``WEEK`` constant.

1.2
---

* Optimize hashing and pickling.

1.1
---

* Add ``YEAR``, ``MONTH``, and ``DAY`` constants.

1.0
---

* Initial stable release.
