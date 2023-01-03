import requests
from flask import Flask,render_template, request

app = Flask(__name__)

#returns the data for the Victoria Line
@app.route('/tflTime', methods = ["POST"])
def victoria():
   #time arrival info for tube line
  
   stationN = request.form['stationName']
   idsline = request.form['ids']
   url = "https://api.tfl.gov.uk/Line/{}/Arrivals".format(idsline)
   response = requests.get(url)
   data = response.json()
   platformN = (data[0] ['platformName'])
   destination = (data[0] ['destinationName'])
   time_S = (data[0]['timeToStation'])
   time_M = int(time_S / 60)
   return render_template('tflTime.html' , line = idsline, sta = stationN ,  dest = destination , time = time_M, platform = platformN )





      
@app.route('/')
def victoriaLine():

  return """
         <html>
  <head>
       <title>  London's Train services. </title>

       <style>
        h1{
   font-color: black;
   font-size: 60px;

   }

       body{ 
   
       background-color: #d3d3d3 ;
      }
   </style>

     <body>
        
        <br>
        <h1><center>Welcome to London's train services</center> </h1>
        <form method="post" action="http://127.0.0.1:5000/tflTime">
         <br>
         <br>
         <br>
           <b><h2><center> Enter tube line:</b>
           <input type = "text" name ="ids"
           <br>
           <br>
           <br>
           <b> Enter Station Name:</b>
           <input type ="text" name="stationName">
           <br>
           <br>
           <input type="submit">
           </center></h2>
        </form>
     </body> 
</html>
"""


if __name__=='__main__':
   app.run(debug=True)