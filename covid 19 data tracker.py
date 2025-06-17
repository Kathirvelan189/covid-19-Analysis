import requests
import matplotlib.pyplot as plt

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        stats = {
            "Total Cases": data["cases"],
            "Today's Cases": data["todayCases"],
            "Total Deaths": data["deaths"],
            "Today's Deaths": data["todayDeaths"],
            "Recovered": data["recovered"],
            "Active": data["active"],
            "Critical": data["critical"],
        }

        print(f"\n🦠 COVID-19 Stats for {data['country']}")
        for key, value in stats.items():
            print(f"{key:15}: {value}")

        plot_covid_data(data['country'], stats)
    else:
        print("❌ Country not found or API error. Please check the name and try again.")

def plot_covid_data(country, stats):
    labels = list(stats.keys())
    values = list(stats.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=['blue', 'cyan', 'red', 'orange', 'green', 'purple', 'brown'])
    plt.title(f"COVID-19 Stats for {country}", fontsize=14)
    plt.xlabel("Categories")
    plt.ylabel("Number of People")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:,}', va='bottom', ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

while True:
    country = input("\nEnter a country name (or type 'exit' to quit): ").strip()
    if country.lower() == 'exit':
        break
    get_covid_data(country)
