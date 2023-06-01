Python Lunch Lab - Quarto Demo
================
Erika Tyagi
10/21/22

<details>
<summary>Code</summary>

``` python
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

pd.set_option('display.max_columns', 100)
sns.set_theme(style="whitegrid")
```

</details>

# Load Data

The “2018 Central Park Squirrel Census - Squirrel Data” (or “The
Squirrel Census”) is a dataset available on the [City of New York’s Open
Data Portal](https://opendata.cityofnewyork.us/). Here’s the description
of the dataset pulled from the portal:

> [The Squirrel Census](https://www.thesquirrelcensus.com/) is a
> multimedia science, design, and storytelling project focusing on the
> Eastern gray (Sciurus carolinensis). They count squirrels and present
> their findings to the public. This table contains squirrel data for
> each of the 3,023 sightings, including location coordinates, age,
> primary and secondary fur color, elevation, activities,
> communications, and interactions between squirrels and with humans.”

<details>
<summary>Code</summary>

``` python
# Load the dataset 
url = "https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv"
df = pd.read_csv(url)

# View the first 3 rows 
df.head(3)
```

</details>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
      <th>Unique Squirrel ID</th>
      <th>Hectare</th>
      <th>Shift</th>
      <th>Date</th>
      <th>Hectare Squirrel Number</th>
      <th>Age</th>
      <th>Primary Fur Color</th>
      <th>Highlight Fur Color</th>
      <th>Combination of Primary and Highlight Color</th>
      <th>Color notes</th>
      <th>Location</th>
      <th>Above Ground Sighter Measurement</th>
      <th>Specific Location</th>
      <th>Running</th>
      <th>Chasing</th>
      <th>Climbing</th>
      <th>Eating</th>
      <th>Foraging</th>
      <th>Other Activities</th>
      <th>Kuks</th>
      <th>Quaas</th>
      <th>Moans</th>
      <th>Tail flags</th>
      <th>Tail twitches</th>
      <th>Approaches</th>
      <th>Indifferent</th>
      <th>Runs from</th>
      <th>Other Interactions</th>
      <th>Lat/Long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-73.956134</td>
      <td>40.794082</td>
      <td>37F-PM-1014-03</td>
      <td>37F</td>
      <td>PM</td>
      <td>10142018</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>+</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>POINT (-73.9561344937861 40.7940823884086)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-73.968857</td>
      <td>40.783783</td>
      <td>21B-AM-1019-04</td>
      <td>21B</td>
      <td>AM</td>
      <td>10192018</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>+</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>POINT (-73.9688574691102 40.7837825208444)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-73.974281</td>
      <td>40.775534</td>
      <td>11B-PM-1014-08</td>
      <td>11B</td>
      <td>PM</td>
      <td>10142018</td>
      <td>8</td>
      <td>NaN</td>
      <td>Gray</td>
      <td>NaN</td>
      <td>Gray+</td>
      <td>NaN</td>
      <td>Above Ground</td>
      <td>10</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>NaN</td>
      <td>POINT (-73.97428114848522 40.775533619083)</td>
    </tr>
  </tbody>
</table>
</div>

# Plot Data

<div>

> **Note**
>
> Note that the `Foraging` variable indicates that the squirrel was seen
> foraging for food.

</div>

<details>
<summary>Code</summary>

``` python
# Create simple barplot 
sns.countplot(
    x="Foraging", 
    hue="Primary Fur Color", 
    data=df 
)

plt.show()
```

</details>

<figure>
<img
src="quarto-pug-demo-squirrels_files/figure-commonmark/squirrels-output-1.png"
id="squirrels" alt="Foraging Patterns, The Squirrel Census (2018)" />
<figcaption aria-hidden="true">Foraging Patterns, The Squirrel Census
(2018)</figcaption>
</figure>
