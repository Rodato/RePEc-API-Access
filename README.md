# RePEc-API-Access


Set of python scripts  to get and process data from RePEc API.

It have made two ways to store the data: on a csv file or in mongodb. I strongly recommended use mongodb, for some reason, it seem that some JSON from the API have problems and when you try to process it with `jsondump` it breaks.

You also should learn to play and consider not made the calls  too close to each other. To spacing them it is usefull the function `time.sleep()`.


To get your access code you have to see the instructions access here: https://ideas.repec.org/api.html.
