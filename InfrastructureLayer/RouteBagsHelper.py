from InfrastructureLayer.DBconfig import DatabaseConfig
from flask_mysqldb import MySQL

app = DatabaseConfig()
mysql = MySQL(app)


def routeBagsHelper():
    cur = mysql.connection.cursor()
    result = cur.execute(
        "select * from bags where `position` != 'Airline Loading Area' and `position` != 'Check In Area'")
    bags = cur.fetchall()
    if result == 0:
        return 'No Bags In The System'

    result = cur.execute(
        "select * from conveyorBelt where `isJammed` = 1")

    jammedBeltPosition = '99'
    if result != 0:
        jammedBelt = cur.fetchall()
        jammedBeltPosition = str(
            jammedBelt[0]['level']) + jammedBelt[0]['type']

    for bag in bags:
        bagPosition = bag['position']
        if bagPosition[0] != jammedBeltPosition[0]:
            bagTagId = bag['bagTagId']
            cur.execute(
                "select flightId from bagTags where `id` = %s", [bagTagId])
            flightId = cur.fetchall()
            cur.execute(
                "select airline from flights where `id` = %s", [flightId[0]['flightId']])
            airline = cur.fetchall()
            destinationRoute = airline[0]['airline']
            if bagPosition[1] == destinationRoute:
                isBeingRouted = False
                cur.execute("UPDATE `bags` SET `position` = %s, `isBeingRouted` = %s  WHERE `id` = %s",
                            ('Airline Loading Area', isBeingRouted, bag['id']))
                mysql.connection.commit()
            else:
                nextPosition = bagPosition[0]
                if bagPosition[1] == 'A':
                    nextPosition += 'B'
                elif bagPosition[1] == 'B':
                    nextPosition += 'C'
                elif bagPosition[1] == 'C':
                    nextPosition += 'D'
                else:
                    nextPosition += 'A'

                cur.execute("UPDATE `bags` SET `position` = %s WHERE `id` = %s",
                            (nextPosition, bag['id']))
                mysql.connection.commit()

    cur.close()
    return 'Bag Routing Updated'


def rerouteHelper(rerouteJammedBags):
    cur = mysql.connection.cursor()
    result = cur.execute(
        "select * from bags where `position` != 'Airline Loading Area' and `position` != 'Check In Area'")
    bags = cur.fetchall()
    if result == 0:
        print('\n\nNo Bags In The System\n\n')

    result = cur.execute(
        "select * from conveyorBelt where `isJammed` = 1")

    jammedBelt = cur.fetchall()
    jammedBeltPosition = str(
        jammedBelt[0]['level']) + jammedBelt[0]['type']

    for bag in bags:
        bagPosition = bag['position']
        if bagPosition[0] == jammedBeltPosition[0] and (bagPosition == jammedBeltPosition) == rerouteJammedBags:
            nextPosition = ''
            if jammedBeltPosition[0] == '1':
                nextPosition = '2A'
            elif jammedBeltPosition[0] == '2':
                nextPosition = '3A'
            else:
                nextPosition = '1A'
            cur.execute("UPDATE `bags` SET `position` = %s WHERE `id` = %s",
                        (nextPosition, bag['id']))
            mysql.connection.commit()

    cur.close()
    return 'Bags Rerouted'
