#!/bin/python3


def find_smallest_positive(xs):
    def go(left, right):
        if len(xs) == 0:
            return None
        if xs[-1] < 0:
            return None
        if left == right:
            if xs[left] > 0:
                return left
            else:
                return None
        mid = (left + right) // 2
        if xs[mid] == 0:
            return mid + 1
        if xs[mid] > 0:
            right = mid
        if xs[mid] < 0:
            left = mid + 1
        return go(left, right)
    return go(0, len(xs) - 1)


def count_repeats(xs, x):
    def upper_bound(xs, x):
        if len(xs) == 0:
            return None
        if xs[0] == x:
            return 0

        def go(left, right):
            if left == right:
                if xs[left] == x:
                    return left
                else:
                    return None
            mid = (left + right) // 2
            if xs[mid] < x:
                right = mid
            if xs[mid] > x:
                left = mid + 1
            if xs[mid] == x:
                if mid == left or xs[mid - 1] > x:
                    return mid
                else:
                    right = mid - 1
            return go(left, right)
        return go(0, len(xs) - 1)

    def lower_bound(xs, x):
        if len(xs) == 0:
            return None
        if xs[-1] == x:
            return len(xs) - 1

        def go(left, right):
            if left == right:
                if xs[right] == x:
                    return right
                else:
                    return None
            mid = (left + right) // 2
            if xs[mid] > x:
                left = mid + 1
            if xs[mid] < x:
                right = mid - 1
            if xs[mid] == x:
                if mid == right or xs[mid + 1] < x:
                    return mid
                else:
                    left = mid + 1
            return go(left, right)
        return go(0, len(xs) - 1)

    upper = upper_bound(xs, x)
    lower = lower_bound(xs, x)
    if upper is None or lower is None:
        return 0
    else:
        return lower - upper + 1


def argmin(f, lo, hi, epsilon=1e-3):
    def go(lo, hi):
        m1 = lo + (hi - lo) / 4
        m2 = hi - (hi - lo) / 4
        if m1 > m2:
            temp = m2
            m2 = m1
            m1 = temp
        if abs(lo - hi) < epsilon:
            return (hi + lo) / 2
        if f(m1) == f(m2):
            lo = m1
            hi = m2
        if f(m1) < f(m2):
            hi = m2
        if f(m1) > f(m2):
            lo = m1
        return go(lo, hi)
    return go(lo, hi)


def find_boundaries(f):
    lo = - 1
    hi = 1
    mid = (lo + hi) / 2
    if f(lo) > f(mid):
        lo *= 2
    elif f(hi) > f(mid):
        hi *= 2
    else:
        return (lo, hi)
    find_boundaries(f)


def argmin_simple(f, epsilon=1e-3):
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
