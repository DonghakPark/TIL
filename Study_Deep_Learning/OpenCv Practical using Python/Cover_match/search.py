from coverdescriptor import CoverDescriptor
from convermatcher import ConverMatcher
import glob
import csv
import cv2
import ntpath

data_path = "books.csv"
book_path ="covers"
query_path = "queries/query02.png"

db = {}

for l in csv.reader(open(data_path)):
    db[l[0]] = l[1:]

cd = CoverDescriptor()
cv = ConverMatcher(cd, glob.glob(book_path + "/*.png"))
query_image = cv2.imread(query_path)
gray = cv2.cvtColor(query_image, cv2.COLOR_BGR2GRAY)
(queryKps, queryDescs) = cd.describe(gray)

results = cv.search(queryKps, queryDescs)
cv2.imshow("Query", query_image)

if len(results) == 0:
    print("I could not find a match for that cover") #error message
    cv2.waitKey(0)
else:
    for (i, (score, book_path)) in enumerate(results):
        (author, title) = db[ntpath.basename(book_path)]
        print("{}. {:.2f}% : {} - {}".format(i+1, score*100, author, title))

        result = cv2.imread(book_path)
        cv2.imshow("Result", result)
        cv2.waitKey(0)

