import mysql.connector

class Database:
    cnx = None

    def connect(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='meet_indexer')
        cursor = self.cnx.cursor()
        return cursor;
        # cnx.close()

    def save_transcription_fragment(self, fragment):
        cursor = self.connect();
        
        query = "INSERT INTO transcription (`id`, `meets_id`, `start_time`, `transcription`, `end_time`) VALUES (%(id)s, %(meets_id)s, %(start_time)s, %(transcription)s, %(end_time)s);"

        cursor.execute(query, fragment)

        self.cnx.commit()
        cursor.close()
        self.cnx.close()

    def __decode_query(self, cursor):
        columns = cursor.description
        data = []
        for value in cursor.fetchall():
            tmp = {}
            for (index,column) in enumerate(value):
                tmp[columns[index][0]] = column
            data.append(tmp)
        return data
    
    def __decode_query_and_get_first_object(self, cursor):
        decoded = self.__decode_query(cursor)
        if(len(decoded) > 0):
            return decoded[0]
        return None

    def search_transcriptions(self, search : str):
        print(search)
        cursor = self.connect();
        query = f"SELECT transcription.id, meets_id, transcription, start_time, video_url FROM transcription INNER JOIN meets ON meets.id = transcription.meets_id WHERE transcription LIKE '%{search}%'"

        cursor.execute(query)

        transcriptions = self.__decode_query(cursor)
        transcriptions = sorted(transcriptions, key=lambda x: x['meets_id'], reverse=True)
        return transcriptions



    def get_raw_transcription(self, meet_id : int):
        cursor = self.connect();
        query = f"SELECT transcription FROM transcription WHERE meets_id = {meet_id} ORDER BY start_time ASC"

        cursor.execute(query)
        completeVideoTranscription = []
        for videoTranscription in cursor.fetchall():
            completeVideoTranscription.append(videoTranscription[0])

        return "".join(completeVideoTranscription)
    
    def list_videos(self):
        cursor = self.connect();
        query = "SELECT id, date, size, video_url, duration FROM meets"

        cursor.execute(query)

        videos = self.__decode_query(cursor)
        videos = sorted(videos, key=lambda x: x['video_url'], reverse=True)

        return videos

        # columns = cursor.description
        # videos = []
        # for value in cursor.fetchall():
        #     tmp = {}
        #     for (index,column) in enumerate(value):
        #         tmp[columns[index][0]] = column
        #     videos.append(tmp)
        # return videos

        # videos = []
        # for videoData in cursor.fetchall():
        #     videos.append(videoData)
        # return videos


    def list_synced_videos(self):
        cursor = self.connect();
        query = "SELECT video_url FROM meets"

        cursor.execute(query)
        videoUrls = []
        for videoUrl in cursor.fetchall():
            videoUrls.append(videoUrl[0])
        return videoUrls

    def load_meet(self, meet_id : int):
        cursor = self.connect();
        
        query = "SELECT id, date, size, video_url, duration FROM meets WHERE id = %s"

        cursor.execute(query, (meet_id,))

        return self.__decode_query_and_get_first_object(cursor)
    
    def load_meet_by_path(self, meet_id : int):
        cursor = self.connect();
        
        query = "SELECT id, date, size, video_url, duration FROM meets WHERE video_url = %s"

        cursor.execute(query, (meet_id,))
        return self.__decode_query_and_get_first_object(cursor)
    
    def save_meet(self, fragment):
        cursor = self.connect();
        
        query = "INSERT INTO meets (`date`, `size`, `video_url`, `duration`) VALUES (%(date)s, %(size)s, %(video_url)s, %(duration)s);"

        cursor.execute(query, fragment)
        meet_id = cursor.lastrowid;
        self.cnx.commit()
        cursor.close()
        self.cnx.close()
        return meet_id