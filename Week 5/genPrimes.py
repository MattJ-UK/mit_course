def genPrimes():
    test_number = 1
    current_primes = []
    while True:
        while True:
            undivided_count = 0
            test_number += 1
            for x in current_primes:
                if test_number % x != 0:
                    undivided_count += 1

            if undivided_count == len(current_primes):
                break

        yield test_number
        current_primes.append(test_number)


