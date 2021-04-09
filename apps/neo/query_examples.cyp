// Load districts
LOAD CSV WITH HEADERS FROM 'file:///districts.csv' AS line
WITH line
match (r:Region{name:line['region']})
merge(d:District{name:line['name'], population:line['population']})-[:BELONGS_TO]->(r)


// Load cities and regions
LOAD CSV WITH HEADERS FROM 'file:///towns.csv' AS line
WITH line
match (district:District{name:line['district']})
merge(place:Town{name:line['name'], population:line['population']})-[:BELONGS_TO]->(district)


// Load cities and regions
LOAD CSV WITH HEADERS FROM 'file:///villages.csv' AS line
WITH line
match (district:District{name:line['district']})
merge(place:Village{name:line['name'], population:line['population']})-[:BELONGS_TO]->(district)


// Find the capitals of the regions.
match (t:Town)-[:CAPITAL_OF]->(r:Region) return t

// Find the neighbour regions of Tavush
match (region:Region{name:'Tavush'})-[:ARE_NEIGHBOURS]-(neighbours:Region) return region, neighbours

//Find the neighbour regions of neighbours Tavush.
match (region:Region{name:'Tavush'})-[:ARE_NEIGHBOURS*..2]-(neighbours:Region) return region, neighbours

// Find 5 possible ways from Shirak to Tavush (trough neighbour regions)
match (region_1:Region{name:'Shirak'}), (region_2:Region{name:"Tavush"}), p = ((region_1)-[:ARE_NEIGHBOURS*..7]-(region_2)) return p Limit 5

// Find the shortest path from Shirak to Tavush (trough neighbour regions)
match (region_1:Region{name:'Shirak'}), (region_2:Region{name:"Tavush"}), p = shortestPath((region_1)-[:ARE_NEIGHBOURS*..7]-(region_2)) return p

// Run the same query with EXPLAIN AND PROFILE



// Get relation between company Volkswagen and China and "Manufacture of motor vehicles, trailers and semi-trailers'
MATCH (company:Company{code:'VOW3 GY Equity'})-[*..2]-(geodiv:GeoDivision)-[*..2]-(reg:Region)-[*..2]-(cn:Country) WITH
company, geodiv, reg, cn limit 3  MATCH (country:Country{name:'China'}), p1=shortestPath((company)-[*..15]-(country)),
(industry:Industry{wiot_code:'C29'}), p3=shortestPath((cn)-[*..5]-(industry)) Return company, geodiv, reg, p1, p3