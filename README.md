<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
 

<h3 align="center">Kryptolert</h3>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Developed using the Flask Framework and other flask extensions. The system I have developed consists of 3 servers. The first server handling the API requests and the other two servers handling the Mailing and Scheduler for checking the coin prices with the alerts. THe system makes use of PostGresQL and RabbitMQ to be more scalable. Since I am not that comfortable with docker and due to time constraints I was not able to setup the docker-compose.yml in time. 

### Build With

* Python
* RabbitMQ
* PostGreSQL

### Packages Used


* Flask
* Flask-SQLAlchemy
* Psycopg2
* Flask-Mail
* Flask-Login
* Flask-Migrate
* Pika
* APScheduler

### File Structure
/root -> Houses the Main API and the Mailing and Scheduler Services as 2 different folders 

/root/mailer -> Mailing Service 

/root/scheduler -> Schduler CRON Job that Checks the PostGresQL database for triggering any alerts 



<!-- USAGE EXAMPLES -->
## Usage

To run the code as of now first start the PostGres and RabbitMQ services. After that start the Main API followed by the scheduler and mailer services.

Requests to the API will create alerts: 
 
 * `/auth/register` - To create a user. `email` and `password` have to be passed in.
 * `/auth/login` - Logs in valid users and returns `token`.
 * `/alerts/create` - Creates a new alert
 * `/alerts/delete` - Deletes an alert
 * `/alerts/fetch_all` - Returns list of all alerts created so far
 * `/alerts/fetch_all/<FILTER>` - Returns the list filtered by status, which can be one of "TRIGGERED", "CREATED", "DELETED"
 

## Examples

Let the input file in every example be [Data.csv](https://github.com/dyte-submissions/dyte-vit-2022-NarayanAdithya/blob/main/Data.csv):
<div align="center">
  <img src="images/input_dat.png" alt="input_dat" >
</div>

<br>
<br>
1. Making a simple check across multiple repo's for single package version
   
   ```sh
   python cli.py -i Data.csv axios@0.22.3
   ```

   The resultant output file output.csv is as follows:

<div align="center">
<img src="images/output_dat_ex1.png" alt="output_dat" >
</div>

<br>
<br>
2. Making a simple check across multiple repo's for multiple package version
   
   ```sh
   python cli.py -i Data.csv axios@0.22.3 express@5.8.4
   ```

   The resultant output file output.csv is as follows:

<div align="center">
<img src="images/output_dat_ex2.png" alt="output_dat" >
</div>
We can see that when the package doesnt exist in package.json the tool automatically assings True to version verification so that it doesn't get committed in case the `-update` flag was present.
<br>
<br>
3. Making a simple check across multiple repo's for multiple package version and making the pull request
   
   ```sh
   python cli.py -i Data.csv axios@0.22.3 express@5.8.4 -update -branch main
   ```
  Code Snippet:
<div align="center">
<img src="images/code_snippet.png" alt="output_dat" >
</div>

   The resultant output file output.csv is as follows:

<div align="center">
<img src="images/pull_request_output.png"  alt="output_dat" >
</div>
We can see that when the package doesnt exist in package.json the tool automatically assings True to version verification so that it doesn't get committed in case the `-update` flag was present.

The Pull requests were made as follows:
<div align="center">
<img src="images/example_pr.png"  alt="output_dat" >
</div>

Similary for the other repositories too...
<br>
<br>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Tasks Done

- [x] Create API Endpoint for creating an alert
- [x] Creating API Endpoint for deleting an alert
- [x] Creating API Endpoint for fetching all alerts
- [x] Creating API Endpoint to return alerts filtered by status
- [ ] Paginate the response
- [x] Add User Authentication with JWT
- [x] Make use of coingecko API for price checking
- [x] Printing the mail procedure to console as google removed access to less secure apps for my account
- [ ] Adding a cache layer for the fetch_all endpoint
- [x] Use PostGres
- [x] Use RabbitMQ
- [ ] Bundle in Docker-Compose





## Contact

Adithya Narayan - [@a.dity.a_n.araya.n](https://www.instagram.com/a.dity.a_n.araya.n/?hl=en) - adithyanarayan1234@gmail.com





[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/adithya-narayan-3747081a3/
[product-screenshot]: images/screenshot.png
