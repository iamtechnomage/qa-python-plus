from time import perf_counter_ns, sleep, time

def divide_func(div):
    try:
        result = 100 / div
    except TypeError as e:
        print(f"Делитель не число. {e.__str__()}")
    except Exception as e:
        print(f"Случилось деление на 0. {e.__str__()}")


if __name__ == "__main__":
    # divide_func(0)
    # divide_func("0")
    # perf_time =
    # perf_time = lambda: perf_counter_ns()
    start_time = perf_counter_ns()
    sleep(1)
    end_time = perf_counter_ns()
    print(start_time)
    print(end_time)

