# Solution
The capitalised words in the challenge prompt ('Over', 'Pass', 'Turbo') is a clue to use Overpass Turbo. It's a data filtering tool for OpenStreetMap (OSM) that allows you to run OSM Queries. 

Text in the provided email3.png ('i doubt anyone will find me even if this picture gets leaked') hints that visual clues in the image provided (apartment.png) are relevant to building our OSM Query.

To learn more about OverPass Turbo, I recommend [this tutorial](https://osm-queries.ldodds.com/tutorial/00-node-1.osm.html), which will suffice for this challenge.

To write an OSM Query we need to first define a search area.

### Identify Country
1. Challenge prompt: "I'm over and pass the border" could refer to country borders, suggesting we are not in Germany anymore
2. The bus stop in apartment.png features a yellow and green circle with the letter "H", which stands for "Haltestelle" (German for 'bus stop'). This unique bus stop symbol is only found in [Germany](https://commons.wikimedia.org/wiki/Category:Bus_stop_signs_in_Germany) and [Austria](https://commons.wikimedia.org/wiki/Category:Bus_stop_signs_in_Austria).

We are likely in Austria.
### Write Query
1. We are looking for a 3-storey residential building in Austria with house number 54, that is near a bus stop with no shelter.
2. Build and run query in [Overpass Turbo](https://overpass-turbo.eu/)
```
// define search area
{{geocodeArea:Austria}}->.searchArea;

// find all buildings that qualify. cast a large net for nodes, ways and relations (nwr)
nwr["building"="residential"]["addr:housenumber"="54"]["building:levels"="3"](area.searchArea);

// find all bus stops near these buildings (10m distance is arbitrary, can be 100m too)
node(around:10.00)["bus"="yes"]["shelter"="no"];

// outputs relevant bus stops
out body;
```
3. The code above will return the location of the bus stop. However, the prompt asks for the **apartment's** coordinates, not the bus stop or the location from which the photo was taken.
4. Apartment Address: 54 St. Veiter Str., Klagenfurt am Wörthersee, Austria. (46.632603, 14.310690)

**Note**: It is still possible to find the location even if your search query is slightly different (i.e. adding/excluding certain parameters). You only need 3 key elements - **house number**, **building levels** and existence of **bus stop**. If you're missing any of these elements, you will have to sift through an impossibly large pool of results.

**Flag: LNC25{46.6326,14.3107}**

### Resources
1. Image Source: [https://maps.app.goo.gl/BUQmcbDV1Dhcy6om7](https://maps.app.goo.gl/BUQmcbDV1Dhcy6om7)
2. OSM Tutorial: [https://osm-queries.ldodds.com/tutorial/00-node-1.osm.html](https://osm-queries.ldodds.com/tutorial/00-node-1.osm.html)
3. Overpass Turbo Wiki Guide: [https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide](https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide)
4. Plonkit: [www.plonkit.net](www.plonkit.net)

### Author's Note (Post-CTF)
One participant reported having to sift through a large pool of results. I believe they likely cast a radius that was too large when searching for bus stops (via the around:xx parameter). In my testing though, even setting around:100 only results in 60+ locations, which is tedious to sift through, but not impossible. Admittedly, OSM is very finnicky to use, because a lot is riding on your specific query, but that's part of the intended difficulty for this challenge.

Someone also managed to cheese this challenge, by reverse image searching the gray building in the corner of the photo. When crafting this challenge, I did check that the location wasn't reverse image searchable, but I should have done more thorough testing.