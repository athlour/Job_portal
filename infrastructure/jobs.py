import pandas as pd


class Jobs:
    def __init__(self):
        self.df = pd.read_excel("C:\\Users\\Athlour\\PycharmProjects\\Job_portal\\infrastructure\\jobs.xlsx")

    '''
    this function return jobs category
    '''
    def jobs_category(self):
        jobs = self.df.loc[:, 'Job Category']
        resource = {}
        result = list(set(jobs))
        resource["jobs_category"] = result
        return resource

    """
    This Function return the list of jobs locations
    """
    def job_locations(self):
        jobs = self.df.loc[:, 'Location']
        resource = {}
        result = list(set(jobs))
        resource["jobs_location"] = result
        return resource

    """
    This Function return the list of Jobs by category  
    """
    def __convery_to_dict__(self, job):
        empty_dict = {}
        head_index = job.head()
        for index in head_index.index:
            row = job.loc[index]
            empty_dict.update({row["Job Code"]: row.to_dict()})
        return empty_dict

    def __jobs_by_category__(self, value):
        #  TODO Process the Data to return jobs dict by category
        jobs = self.df.loc[self.df['Job Category'] == value]
        common = self.__convery_to_dict__(jobs)
        return common

    """
    This Function return the list of Jobs by location  
    """
    def __job_by_locations__(self, value):
        print("this line runs ", value)
        #  TODO Process the Data to return jobs dict by location
        jobs = self.df.loc[self.df['Location'] == value]
        print(jobs)
        common = self.__convery_to_dict__(jobs)
        return common

    """
    This Function return the list of Jobs by Date Posted  
    """
    def __by_date__(self, value):
        #  TODO Process the Data to return jobs dict by date
        jobs = self.df.loc[self.df['Date posted'] == value]
        common = self.__convery_to_dict__(jobs)
        return common

    """
    This Function return the list of Jobs by Open  
    """
    def __by_status__(self, value):
        #  TODO Process the Data to return jobs dict by open
        jobs = self.df.loc[self.df['Status'] == value]
        common = self.__convery_to_dict__(jobs)
        return common

    def all_jobs(self, condition, values):
        by = str(condition)
        print(type(by))
        print("this Line runs ")
        return self.__job_by_locations__(values)
        """ 
        if by is "location":
            print("1")
            print(by, values)
            
        elif by == "category":
            return self.__jobs_by_category__(values)
        elif by == "date":
            return self.__by_date__(values)
        elif by == "status":
            return self.__by_status__(values)
        """