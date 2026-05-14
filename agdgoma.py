year = int(input("Enter a year: "))

N = int(input("Enter the number of iterations: "))


def easter(year, N):
    with open("Easter_dates.txt", "a") as f:
        for i in range(N):
            a = year % 19
            b = year % 4
            c = year % 7
            k_c = year // 100
            p_c = (13 + (8 * k_c)) // 25
            q_c = k_c // 4
            M_c = (15 - p_c + k_c - q_c) % 30
            N_c = (4 + k_c - q_c) % 7
            d_c = ((19 * a) + M_c) % 30
            e_c = ((2 * b) + (4 * c) + (6 * d_c) + N_c) % 7

            r_c = 22 + d_c + e_c

            if r_c < 32:
                day_c = r_c
                month_c = "March"
            else:
                if d_c == 29 and e_c == 6:
                    day_c = 19
                elif d_c == 28 and e_c == 6 and (((11 * M_c) + 11) % 30) < 19:
                    day_c = 18
                else:
                    day_c = r_c - 31
                month_c = "April"

            f.write(
                f"------------------------\nThe date of Catolic Easter {year} is {day_c} {month_c}.\n"
            )

            M_o = 15
            N_o = 6

            d_o = ((19 * a) + M_o) % 30
            e_o = ((2 * b) + (4 * c) + (6 * d_o) + N_o) % 7

            r_o = 22 + d_o + e_o

            C = year // 100
            H = C - (C // 4) - 2

            if r_o > 61 - H:
                day_o = r_o - 61 + H
                month_o = "May"
                f.write(
                    f"The date of Ortodox Easter {year} in Julian calendar {r_o} march, translater from Julian to Gregorian {H}, The date of Ortodox Easter {year} in grigorian calendar {r_o} - 61 + {H}  = {day_o} {month_o}.\n"
                )
            elif (r_o - 31 + H) < 1:
                day_o = r_o + 1
                month_o = "March"
                f.write(
                    f"The date of Ortodox Easter {year} in Julian calendar {r_o} march, translater from Julian to Gregorian {H}, The date of Ortodox Easter {year} in grigorian calendar {r_o} + {H}  = {day_o} {month_o}.\n"
                )
            else:
                day_o = r_o - 31 + H
                month_o = "April"
                f.write(
                    f"The date of Ortodox Easter {year} in Julian calendar {r_o} march, translater from Julian to Gregorian {H}, The date of Ortodox Easter {year} in grigorian calendar {r_o} - 31 + {H}  = {day_o} {month_o}.\n"
                )

            year += 1


easter(year, N)
