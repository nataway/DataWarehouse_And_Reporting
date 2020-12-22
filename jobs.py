import pandas as pd
import dao

def insertIntoJobs(tableName):

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()

    df = pd.read_csv(f"{tableName}.csv") 
    df.fillna("", inplace=True)

    for index, row in df.iterrows():
        # print(type(row["8"]), row["8"])
        try:
            cursor.execute("""INSERT INTO [dbo].[ST_JOBS]([JOB_ID]
                                                ,[JOB_TITLE]
                                                ,[MIN_SALARY]
                                                ,[MAX_SALARY]
                                                ) 
                                    values(?,?,?,?)"""
                                , row["0"], row["1"], row["2"], row["3"]
                                )
        except Exception as e:
            print(type(str(e)))
            
    cnxn.commit()
    cursor.close()
    cnxn.close()