# Импортируйте всё необходимое:
from decimal import Decimal, getcontext

# Установите требуемую точность вычислений:
getcontext().prec = 3


# Допишите код функции.
def get_monthly_payment(total_sum, months_count, percents):
    # Подсчитайте основную сумму ежемесячного платежа, без учёта процентов:
    monthly_raw = Decimal(total_sum) / Decimal(months_count)

    # Подсчитайте ежемесячный платёж по процентам банка,
    # исходя из ежемесячной части основной суммы и процентной ставки:
    monthly_addition = (Decimal(total_sum) * Decimal(percents) / Decimal(100)) / Decimal(months_count)

    # Подсчитайте общую сумму ежемесячного платежа:
    total_per_month =  Decimal(monthly_raw + monthly_addition)
    # Верните общую сумму ежемесячного платежа:
    return total_per_month


payment_value = get_monthly_payment(54, 24, 9)
print('Ежемесячный платёж:', payment_value, 'ВтК.')