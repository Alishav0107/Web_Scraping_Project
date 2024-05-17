from src.appConfig import getAppConfigDict
from src.ScrapeIMDb import generateExcelFile
from src.sentMail import sendEmail

configDict = getAppConfigDict()

generateExcelFile()

filePath = configDict['excelPath'] +'IMDB_Movie_Rating.xlsx'
isMailSent = sendEmail(configDict, 'Dummy mail', 'hi regards', filePath)