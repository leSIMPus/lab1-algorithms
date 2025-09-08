import pandas as pd
df = pd.read_csv('titanic.csv')
                            # 1: первичный осмотр
print(df.head(7))
print(df.info())                #пропуски есть в столбцах 2 (возраст) и 3(цена билета)
print(df[['Возраст', 'Цена билета']].describe())           #ср. возраст - 19 ср. цена - 1837


                            # 2: Очистка данных.....
df['Возраст'] = df['Возраст'].fillna(19)
print(df.head(7))

def get_age_group(Возраст):
    if Возраст < 18:
        return "Ребёнок"
    elif 18 < Возраст < 65:
        return "Взрослый"
    else:
        return "Пожилой"

df['Звание'] = df['Возраст'].apply(get_age_group)
print(df.head(7))




