import pandas as pb
import matplotlib.pyplot as plt


def open_file(file):
    return pb.read_csv(file)


def the_number_of_lines_in_the_file(data):
    print(f'Кількість рядків у файлі - {data.shape[0]}')


def year_of_observation(data):
    print(f'Скільки років ведеться спосткереження - '
          f'{int(data["Quarter"].max()[:4]) - int(data["Quarter"].min()[:4])}')


def branch_of_economy(data):
    print(f'Кількість галузей економіки за якими велось спостереження - '
          f'{data.drop_duplicates("Description").shape[0]}')


def total_GDP_Amount(series_overall_amount):
    df_overall_amount_index = pb.DataFrame(series_overall_amount).reset_index()
    table = df_overall_amount_index.rename(
        columns={'Description': 'Галузь', 'Amount': 'Загальний ВВП'})

    print(f'Загальний обсяг(Amount) ВВП що отримала кожна окрема '
          f'галузь за всі ці роки спостереженнь: \n" {table}')


def the_maximum_amount_of_GDP(branch_max_amount):
    print(
        f"Галузь, що отримала найбільший обяг ВВП за всі роки спостереження \n"
        f"{branch_max_amount.index[0]}\n"
        f"Обсяг ВВП склав: \n"
        f"{branch_max_amount['Prof, scientific, and technical services']}")


def the_largest_share_in_the_economy(branch_max_amount, data):
    data_sum = data['Amount'].sum()
    max_industry = branch_max_amount['Prof, scientific, and technical services']
    print(f"{branch_max_amount.index[0]} займає {max_industry / data_sum * 100}"
          f" % економіки за весь період спостереження")


def the_industry_biggest_growth(data):
    PT_description_quarter = \
        pb.pivot_table(data, values=['Amount'], index=['Description'],
                       columns=['Quarter'], aggfunc=sum)
    PT_description_quarter['growth_amount'] = \
        PT_description_quarter[('Amount', '2022Q1')] - PT_description_quarter[
            ('Amount', '1987Q2')]
    maxy = \
        PT_description_quarter[
            PT_description_quarter['growth_amount'] == PT_description_quarter[
                'growth_amount'].max()]

    print(
        f'Галузь, що показала найбільше зростання від першого до останього року'
        f'спостереження: {maxy["growth_amount"].index[0]}'
        f'Зростання склало:'
        f' {maxy["growth_amount"]["Prof, scientific, and technical services"]}')


def main():
    data = open_file('/Users/olegbondar/Python/venv/Lessons/Gross.csv')

    the_number_of_lines_in_the_file(data)
    year_of_observation(data)
    branch_of_economy(data)

    series_overall_amount = data.groupby('Description')['Amount'].sum()
    total_GDP_Amount(series_overall_amount)
    max_GDP = series_overall_amount[
        series_overall_amount == series_overall_amount.max()]
    the_maximum_amount_of_GDP(max_GDP)
    the_largest_share_in_the_economy(max_GDP, data)
    the_industry_biggest_growth(data)

    plt.pie(series_overall_amount, labels=series_overall_amount.index)
    plt.savefig('Gross2')


if __name__ == '__main__':
    main()
