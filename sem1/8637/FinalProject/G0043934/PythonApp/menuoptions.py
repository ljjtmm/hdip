from dbconnections import *

def view_cities_by_country():

    country = input("Enter Country: ")

    query = """
        SELECT cy.Name, ci.Name, ci.District, ci.Population 
        FROM city ci 
        INNER JOIN country cy ON ci.CountryCode = cy.Code
        WHERE cy.Name LIKE '%{}%';
    """.format(country)

    df = run_in_mysql(query)

    rows_per_iteration = 2
    total_rows = len(df)
    i = 0
    
    while i < total_rows:
        for index, row in df.iloc[i:i+rows_per_iteration].iterrows():
            print(f"{row['Name']} | {row['ci.Name']} | {row['District']} | {row['Population']}")
        
        i += rows_per_iteration
        
        if i < total_rows:
            user_input = input("-- Quit (q) --")
            if user_input.lower() == 'q':
                break

def update_city_pop():
    city_id = input("Enter City ID: ")

    query = """
        SELECT *
        FROM city
        WHERE ID = %s
    """ % city_id

    df = run_in_mysql(query)

    # Check if city exists
    if df.empty:
        print("City not found.")
        return df

    # Get the first row (assuming city ID is unique)
    city_details = df.iloc[0]  
    city_info = f"{city_details['ID']} | {city_details['Name']} | {city_details['CountryCode']} | {city_details['Population']} | {city_details['latitude']} | {city_details['longitude']}"
    print(city_info)

    update = input("[I]ncrease or [D]ecrease Population: ").upper()

    if update == 'I':
        increase = int(input("Enter Population Increase: "))
        new_population = city_details['Population'] + increase
        query = f"""
            UPDATE city
            SET Population = {new_population}
            WHERE ID = {city_id}
        """
        run_in_mysql(query)
        conn.commit()
        print(f"Population increased to {new_population}")

    elif update == 'D':
        decrease = int(input("Enter Population Decrease: "))
        new_population = city_details['Population'] - decrease
        query = f"""
            UPDATE city
            SET Population = {new_population}
            WHERE ID = {city_id}
        """
        run_in_mysql(query)
        conn.commit()
        print(f"Population decreased to {new_population}")

    else:
        print("Invalid option.")
        return df
    
    return df

def add_new_person():
    print("Add New Person")
    print("-" * 14)

    person_id = input("ID: ")
    name = input("Name: ")
    age = input("Age: ")
    salary = input("Salary: ")
    city = input("City: ")

    # Check if the person ID already exists
    id_query = f"SELECT COUNT(*) AS count FROM person WHERE personID = '{person_id}'"
    id_count = run_in_mysql(id_query).iloc[0]['count']

    if id_count > 0:
        print("Error: Person with this ID already exists.")
        return

    # Check if the city exists
    city_query = f"SELECT COUNT(*) AS count FROM city WHERE Name = '{city}'"
    city_count = run_in_mysql(city_query).iloc[0]['count']

    if city_count == 0:
        print("Error: City does not exist.")
        return

    # Insert new person into the database
    query = f"""
        INSERT INTO person (personID, personname, age, salary, city)
        VALUES ('{person_id}', '{name}', '{age}', '{salary}', '{city}')
    """

    try:
        run_in_mysql(query)
        conn.commit()

        print("New person added successfully.")

    except Exception as e:
        print("An error occurred while adding the new person:", e)

    return

def delete_person():
    person_id = input("Enter ID of Person to Delete: ")

    # Check if the person has visited any cities
    visit_query = f"SELECT COUNT(*) AS count FROM hasvisitedcity WHERE personID = '{person_id}'"
    visit_count_df = run_in_mysql(visit_query)
    visit_count = visit_count_df.iloc[0]['count']

    if visit_count > 0:
        print(f"Can't delete Person ID: {person_id}. He/she has visited cities.")
        return

    # If the person has not visited any cities, proceed with deletion
    delete_query = f"DELETE FROM person WHERE personID = '{person_id}'"

    try:
        run_in_mysql(delete_query)
        conn.commit()
        print("Person deleted successfully.")
    except Exception as e:
        print(e)

    return

def view_countries():
    print("Countries by Pop: ")
    print("-" * 16)

    condition = None
    while condition not in ['<', '>', '=']:
        condition = input("Enter < > or = : ")

    population = input("Enter population: ")

    try:
        population = int(population)
    except ValueError:
        print("Invalid population. Please enter a valid integer.")
        return

    query = f"""
        SELECT *
        FROM country
        WHERE Population {condition} {population};
    """

    df = run_in_mysql(query)

    country_info = ""
    for index, row in df.iterrows():
        country_info += f"{row['Code']} | {row['Name']} | {row['Continent']} | {row['Region']} | {row['SurfaceArea']} | {row['IndepYear']} | {row['Population']} | {row['LifeExpectancy']} | {row['GNP']} | {row['LocalName']} | {row['GovernmentForm']} | {row['HeadOfState']} | {row['Capital']}\n"

    print(country_info)

def twinned_cities():
    query = """
    MATCH (c1:City)-[:TWINNED_WITH]->(c2:City)
    RETURN c1.name AS city1, c2.name AS city2
    UNION
    MATCH (c1:City)-[:TWINNED_WITH]->(c2:City)
    RETURN c2.name AS city1, c1.name AS city2
    """

    output = run_in_neo4j(query)

    if output is None:
        print("Error: No result returned from the database.")
        return

    # Use a set to store unique city pairs
    unique_city_pairs = set()
    for record in output:
        city1 = record['city1']
        city2 = record['city2']
        unique_city_pairs.add((city1, city2))
        unique_city_pairs.add((city2, city1))  # Also include the reverse direction

    # Sort the unique city pairs alphabetically
    sorted_city_pairs = sorted(unique_city_pairs)

    # Print the formatted output
    for city1, city2 in sorted_city_pairs:
        print(f"{city1} <-> {city2}")

def twinned_with_dublin():
    # Prompt the user to enter a City ID
    city_id = input("Enter ID of City to twin with Dublin: ")

    dublin_query = "MATCH (c:City {name: 'Dublin'}) RETURN c"
    dublin_result = run_in_neo4j(dublin_query)
    
    if not dublin_result:
        print("Error: Dublin does not exist in Neo4j database.")

    else:
        # Query to check if the city ID exists in the database
        query = f"MATCH (c:City {{cid: {city_id}}}) RETURN c.name AS name"
        
        # Execute the query to check if the city ID exists and retrieve its name
        city_result = run_in_neo4j(query)


        # Query to twin the city with Dublin
        twin_query = f"MATCH (c:City {{cid: {city_id}}}), (d:City {{cid: 1447}}) CREATE (c)-[:TWINNED_WITH]->(d)"

        #Cover Scenario 2 and 3
        if city_result:
            name = city_result[0]["name"]  # Extract the name from the result

            # Execute the query to twin the city with Dublin
            run_in_neo4j(twin_query)

            print(f"Dublin is now twinned with {name}.")

        #Cover Scenario 1
        else:
            mssql_query = f"SELECT * FROM city where ID = {city_id}"

            mssql_result = run_in_mysql(mssql_query)


            #Cover error scenario 1
            if not mssql_result:
                print(f"Error: City ID: {city_id} doesn't exist in the MySQL database.")

            else:
                city_name = mssql_result['Name'][0].strip("0 ")

                neo4j_insert_query = f"CREATE (c:City {{cid: {city_id}, name: '{city_name}'}})"

                run_in_neo4j(neo4j_insert_query)

                run_in_neo4j(twin_query)