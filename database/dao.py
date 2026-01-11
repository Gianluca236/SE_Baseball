from database.DB_connect import DBConnect
from model.team import Team


class DAO:
    @staticmethod
    def get_team():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t.id, t.year, t.team_code, t.name , sum(s.salary) as salari
                    FROM team t , salary s 
                    WHERE   t.id =s.team_id 
                    GROUP BY t.id """

        cursor.execute(query)

        for row in cursor:
            team=Team(row['id'], row['year'], row['team_code'], row['name'], row['salari'])
            result[team.id] = team

        cursor.close()
        conn.close()
        return result