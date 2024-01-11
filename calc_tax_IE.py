# MODEL
#############################################################################################################
class Salary:

    def get_salary(self) -> float:
        try:
            gross_salary = str(input('Type your gross salary: ')).replace(',','.')
            for letter in gross_salary:
                if not letter.isdigit() and letter != '.':
                    raise ValueError
        except:
            print('\033[31mINVALID VALUE\033[m')
        else:
            self._salary = gross_salary


# CONTROLLER
#############################################################################################################
class IrelandTax:

    def __init__(self, salary: Salary) -> None:
        self.__salary = float(salary._salary)

    def get_salary(self) -> float:
        prsi = self.get_prsi()
        usc = self.get_usc()
        itp = self.get_itp()
        self.show_payroll(self.__salary, prsi, usc, itp)

    def get_prsi(self) -> float:
        if self.__salary > 352:
            prsi = (self.__salary * 4)/100
            show = str(input('Do you want to see the detailed PRSI [Y/N]? ')).upper().strip()[0]
            if show == 'Y':
                print(f'\033[44m{"DESCRIPTION OF THE FEES":^50}\033[m')
                print(f'{"SALARY PER WEEK":<25}{"RATE":<8}{"AMOUNT":<16}')
                print(f'€ {self.__salary:<23.2f}{"4 %":<8}€ {prsi:<16.2f}')
                print(f'\033[32m{"If you earn over € 352 per week":<20}\033[m')
            return prsi
        else:
            return 0
    
    def get_usc(self):
        total = self.__salary * 52
        if total <= 12012: return 0
        if total >= 12012:
            usc1 = (12012 * 0.5) / 100
            total1 = total - 12012
            sum_usc = usc1
            if total1 > 13748:
                usc2 = (13748 * 2) / 100
                total2 = total1 - 13748
                sum_usc += usc2
                if total2 > 44284:
                    usc3 = (44284 * 4) / 100
                    total3 = total2 - 44284
                    sum_usc += usc3
                    if total3 > 0:
                        usc4 = (total3 * 8) / 100
                        total3 = 0
                        sum_usc += usc4
                elif total2 <= 44284:
                    usc3 = (total2 * 4) / 100
                    total3 = 0
                    sum_usc += usc3
            elif total1 <= 13748:
                usc2 = (total1 * 2) / 100
                total2 = 0
                sum_usc += usc2
        tot_usc = sum_usc / 52
        show = str(input('Do you want to see the detailed USC [Y/N]? ')).upper().strip()[0]
        if show == 'Y':
            print(f'\033[44m{"USC TABLE":^50}\033[m')
            print(f'{"ANUAL WAGE":<25}{"AMOUNT":<16}{"RATE":<8}')
            print(f'€ {total:<23.2f}€ {sum_usc:<14.2f}{"???":<5}%')
            print(f'\033[44m{"DESCRIPTION OF THE FEES":^50}\033[m')
            if total > 12012:
                print(f'0.5% {"on the first":<20}€ {"12012,00":<14}€ {usc1:.2f}')
                res1 = total - 12012
                if res1 > 13748:
                    print(f'2.0% {"on the next":<20}€ {13748:<14.2f}€ {usc2:.2f}')
                    res2 = res1 - 13748
                    if res2 > 44284:
                        res3 = res2 - 44284
                        print(f'4.0% {"on the next":<20}€ {44284:<14.2f}€ {usc3:.2f}')
                        if res3 > 0:
                            print(f'8.0% {"over 70,044.01":<20}€ {res3:<14.2f}€ {usc4:.2f};')
                    elif res2 < 44284:
                        print(f'4.0% {"on the next":<20}€ {res2:<14.2f}€ {usc3:.2f}')
                elif res1 < 13748:
                    print(f'2.0% {"on the next":<20}€ {res1:<14.2f}€ {usc2:.2f}')
        return tot_usc

    def get_itp(self):
        relief = (1875 + 1875) / 52
        percent = (self.__salary * 20) / 100
        itp = percent - relief
        if percent < 72.12: return 0
        show = str(input('Do you want to see the detailed INCOME TAX PAID [Y/N]? ')).upper().strip()[0]
        if show == 'Y':
            print(f'\033[44m{"DESCRIPTION OF THE FEES":^50}\033[m')
            print(f'{"Single Person":<36}{"€ 42000":<9}year\n{"":<36}{"€ 807.70":<9}week')
            print(f'\n{"Single persons Tax Credit in 2024":<36}{"€ 1,875":<9}year')
            print(f"{'Employee Tax Credit in 2024':<36}{'€ 1,875':<9}year")
            print(f'\n{"Total Tax Credit Relief":<36}{"€ 3,750":<9}year\n{"":<36}{"€ 72.12":<9}week')
            print(f'\nTo calculate:\nTax = (20% of the income under 42000) - relief')
            print(f'\n\033[32mYour taxable amount € {itp:.2f}\033[m')
        return itp

    def show_payroll(self, gross_salary=0, prsi=0, usc=0, itp=0) -> None:
        from datetime import datetime
        print(f'\033[34m='*50, '\033[m')
        print(f'\033[34m| \033[m\033[44m{"YOUR DETAILED PAYROLL":^46}\033[m\033[34m |\033[m')
        print(f'\033[34m='*50, '\033[m')
        print(f'\033[34m| \033[m{"":<46}\033[34m |\033[m')
        print(f'\033[34m| \033[m\033[1m{"GROSS SALARY":<35}€ {gross_salary:<10.2f}\033[34m| \033[m')
        print(f'\033[34m| \033[m{"PAY RELATED SOCIAL INSURANCE":<35}€ {prsi:<10.2f}\033[34m| \033[m')
        print(f'\033[34m| \033[m{"UNIVERSAL SOCIAL CHARGE":<35}€ {usc:<10.2f}\033[34m| \033[m')
        print(f'\033[34m| \033[m{"INCOME TAX PAID (PAYE)":<35}€ {itp:<10.2f}\033[34m| \033[m')
        data = datetime.today()
        data = data.strftime('%H:%M - %d/%m/%Y')
        tot_deds = prsi + usc + itp
        net_pay = gross_salary - tot_deds
        print(f'\033[34m| \033[m{"TOTAL DEDUCTIONS":<35}€ \033[31m{tot_deds:<10.2f}\033[34m| \033[m')
        print(f'\033[34m| \033[m{"":<46}\033[34m |\033[m')
        print(f'\033[34m| \033[m{"NET PAY":<35}€ \033[32m{net_pay:<10.2f}\033[34m| \033[m')
        print(f'\033[34m| \033[m{"":<46}\033[34m |\033[m')
        print(f'\033[34m| \033[m{"":<46}\033[34m |\033[m')
        print(f'\033[34m| \033[m{data:^46}\033[34m |\033[m')
        print(f'\033[34m='*50, '\033[m')


# VIEW
#############################################################################################################
salary = Salary()
salary.get_salary()
ireland_tax = IrelandTax(salary)
ireland_tax.get_salary()