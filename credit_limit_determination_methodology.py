print('Желаемый срок кредита (в годах):')
term = int(input())

print('Основной ежемесячный доход основного заёмщика:')
aInc1 = int(input())
print('Количество иждивенцев:')
KolIzhd = int(input())
print('Платёж по кредитам Банка основного заёмщика:')
aExpBank1 = int(input())
print('Совокупный платёж по кредитам основного заёмщика, который клиент указал в анкете:')
aExpAnk1 = int(input())
print('Совокупный платёж по кредитам других банков основного заёмщика:')
aExpBKI1 = int(input())

LimitMA = (aInc1 - KolIzhd * 0.09 - aExpBank1 - aExpAnk1 - aExpBKI1) * term * 12

print('Участвует ли в сделке супруга заёмщика? Да/Нет')
answer = input()
if answer == 'Да':
    print('Основной ежемесячный доход супруги заёмщика:')
    aInc2string = input()                                # string
    if aInc2string != '':                                # если введена пустая строка,
        aInc2 = int(aInc2string)                         # то преобразовываем string в int
        if aInc2 >= 0:
            print('Платёж по кредитам Банка супруги заёмщика:')
            aExpBank2 = int(input())
            print('Совокупный платёж по кредитам супруги заёмщика, который клиент указал в анкете:')
            aExpAnk2 = int(input())
            print('Совокупный платёж по кредитам других банков супруги заёмщика:')
            aExpBKI2 = int(input())
            LimitSP = (aInc2 * 0.5 - KolIzhd * 0.03 - aExpBank2 - aExpAnk2 - aExpBKI2) * term * 12
            Limit = LimitMA + LimitSP * 0.3
            print('Совокупный лимит кредитования для всех участников сделки:', Limit)
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
else:
    print('Максимальный лимит кредитования для основного заёмщика:', LimitMA)