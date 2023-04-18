import time
from itertools import zip_longest
from timeit import timeit

import numpy as np


def foo1():
    days_amount, events_amount = map(int, [3, 4])

    days_cost = [0]*days_amount

    for event in [[1, 2, 2], [2, 3, 3], [2, 2, 1], [2, 2, 4]]:
        event_start_day, event_end_day, event_cost = map(int, event)
        for j in range(event_start_day-1, event_end_day):
            if event_cost > days_cost[j]:
                days_cost[j] = event_cost

    result = sum(days_cost)

    #print(result)

def fin1():
    days_amount, events_amount = map(int, input().split())

    days_cost = [0]*days_amount

    for _ in range(events_amount):
        event_start_day, event_end_day, event_cost = map(int, input().split())
        for j in range(event_start_day-1, event_end_day):
            if event_cost > days_cost[j]:
                days_cost[j] = event_cost

    print(sum(days_cost))

def foo2():
    days_amount, events_amount = map(int, [3, 4])

    days_cost = [0]*days_amount

    for event in [[1, 2, 2], [2, 3, 3], [2, 2, 1], [2, 2, 4]]:
        event_start_day, event_end_day, event_cost = map(int, event)
        for j in range(event_start_day-1, event_end_day):
            days_cost[j] = max(days_cost[j], event_cost)

    result = sum(days_cost)

    #print(result)

def foo3():
    days_amount, events_amount = map(int, [3, 4])

    result = sum(
        map(
            max, zip(
                *(
                [0]*(event[0]-1) + [event[2]]*(event[1]-event[0]+1) + [0]*(days_amount-event[1])
                for event in [[1, 2, 2], [2, 3, 3], [2, 2, 1], [2, 2, 4]]
                )
            )
        )
    )

    #print(result)

def fin3():
    days_amount, events_amount = map(int, input().split())

    print(
        sum(
            map(
                max, zip(
                    *(
                    [0]*(start_day-1) + [cost]*(end_day-start_day+1) + [0]*(days_amount-end_day)
                    for start_day, end_day, cost in (
                        map(
                            int, input().split()
                            ) for _ in range(
                                events_amount
                            )
                        )
                    )
                )
            )
        )
    )


def foo4():
    days_amount, events_amount = map(int, [3, 4])
    timetable = [[]]*days_amount
    for event in [[1, 2, 2], [2, 3, 3], [2, 2, 1], [2, 2, 4]]:
        event_start_day, event_end_day, event_cost = map(int, event)
        for i in range(event_start_day, event_end_day):
            timetable[i].append(event_cost)

    result = sum(map(max, timetable))

    #print(result)

def fin4():
    days_amount, events_amount = map(int, input().split())
    timetable = [[]]*days_amount
    for _ in range(events_amount):
        event_start_day, event_end_day, event_cost = map(int, input().split())
        for i in range(event_start_day, event_end_day):
            timetable[i].append(event_cost)

    print(sum(map(max, timetable)))

def foo5():
    days_amount, events_amount = map(int, [3, 4])
    costs = [0]*days_amount
    events = [tuple(map(int, event)) for event in [[1, 2, 2], [2, 3, 3], [2, 2, 1], [2, 2, 4]]]
    events.sort(key=lambda x: x[2], reverse=True)

    for start_day, end_day, event_cost in events:
        for day in range(start_day-1, end_day):
            costs[day] = max(costs[day], event_cost)
        if 0 not in costs:
            break

    result = sum(costs)

    # print(result)

def fin5():
    days_amount, events_amount = map(int, input().split())
    costs = [0]*days_amount
    events = [tuple(map(int, input().split())) for _ in range(events_amount)]
    events.sort(key=lambda x: x[2], reverse=True)

    for start_day, end_day, event_cost in events:
        for day in range(start_day-1, end_day):
            costs[day] = max(costs[day], event_cost)
        if 0 not in costs:
            break

    print(sum(costs))

def foo6():
    days_amount, events_amount = map(int, [3, 4])
    costs = [0]*days_amount
    events = [tuple(map(int, event)) for event in [[1, 2, 2], [2, 3, 3], [2, 2, 1], [2, 2, 4]]]
    events.sort(key=lambda x: x[2], reverse=True)

    done_start = events[0][0]-1
    done_end = events[0][1]-1
    for start_day, end_day, cost in events:
        if start_day-1 == done_start:
            costs[done_start] = max(costs[done_start], cost)
        if end_day-1 == done_end:
            costs[done_end] = max(costs[done_end], cost)
        for i in range(start_day-1, done_start):
            costs[i] = cost
        for i in range(done_end+1, end_day):
            costs[i] = cost
        if start_day-1 < done_start:
            done_start = start_day-1
        if end_day-1 > done_end:
            done_end = end_day-1
        if done_start == 0 and done_end == days_amount - 1:
            break

    result = sum(costs)

    #print(result)

def fin6():
    days_amount, events_amount = map(int, input().split())
    costs = [0]*days_amount
    events = [tuple(map(int, input().split())) for _ in range(events_amount)]
    events.sort(key=lambda x: x[2], reverse=True)

    done_start = events[0][0]-1
    done_end = events[0][1]-1
    for start_day, end_day, cost in events:
        if start_day-1 == done_start:
            costs[done_start] = max(costs[done_start], cost)
        if end_day-1 == done_end:
            costs[done_end] = max(costs[done_end], cost)
        for i in range(start_day-1, done_start):
            costs[i] = cost
        for i in range(done_end+1, end_day):
            costs[i] = cost
        if start_day-1 < done_start:
            done_start = start_day-1
        if end_day-1 > done_end:
            done_end = end_day-1
        if done_start == 0 and done_end == days_amount - 1:
            break

    print(sum(costs))

print(timeit(foo1, globals=globals(), number=10000))
print(timeit(foo2, globals=globals(), number=10000))
print(timeit(foo3, globals=globals(), number=10000))
print(timeit(foo4, globals=globals(), number=10000))
print(timeit(foo5, globals=globals(), number=10000))
print(timeit(foo6, globals=globals(), number=10000))
