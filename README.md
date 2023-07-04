<h2>Odoo16</h2>
<div style="display: inline_block">
    <img align="center" alt="Home-Page" height="200" width="400" src="https://github.com/Ruben-JR/odoo16/assets/75695011/e033b191-caab-41ab-b0db-937eabbc9951">
</div>

<hr>

<h3>About the project</h3>
<p>Odoo is a suite of open source business apps that cover all your company needs: CRM, eCommerce, accounting, inventory, point of sale, project management, etc.

Odoo's unique value proposition is to be at the same time very easy to use and fully integrated.</p>

<hr>

<h3>Objective</h3>
<p>The goal of this project is to create a stock software of products for a laboratory, this has as an objective to practice my knowledge in this technology and become a better developer every day.</p>

<hr>

<h3>Technology used</h3>
<p><div style="display: inline_block">
  <img align="center" alt="Ruben-git" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />
  <img align="center" alt="Ruben-git" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg" />
  <img align="center" alt="Ruben-odoo" height="30" width="60" src="https://user-images.githubusercontent.com/75695011/184119597-9fbb632f-7220-4363-b012-e148930daa2f.png">
  <img align="center" alt="Ruben-odoo" height="30" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg">
</div></p>

<hr>
<h3>NOTE:</h3>
<p>You can follow the documentation inside odoo site to config odoo<a  href="https://www.odoo.com/">here.</a></p>

<hr>

<h3>Getting started</h3>
<h4>Pre-requisites</h4>
<p>Odoo uses PostgreSQL as database management system. Use your package manager to download and install PostgreSQL (supported version: 10.0 and later).
By default, the only user is postgres but Odoo forbids connecting as postgres, so you need to create a new PostgreSQL user</a></p>

<hr>

<h4>Installing</h4>
<p>Cloning the repository</p>

```
git clone https://github.com/Ruben-JR/odoo16
```

<hr>

<h4>Installing dependencies</h4>

For libraries using native code, it is necessary to install development tools and native dependencies before the Python dependencies of Odoo. They are available in -dev or -devel packages for Python, PostgreSQL, libxml2, libxslt1, libevent, libsasl2 and libldap2.

On Debian/Ubuntu, the following command should install all the required libraries:
```
sudo apt install python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev
```

Odoo dependencies are listed in the requirements.txt file located at the root of the Odoo community directory.
Navigate to the path of your Odoo Community installation (Community Path) and run pip on the requirements file
```
$ cd /CommunityPath
$ pip install setuptools wheel
$ pip install -r requirements.txt
```

Download and install nodejs and npm with your package manager.
Install rtlcss
```
sudo npm install -g rtlcss
```

<hr>

<h4>Running odoo</h4>

Once all dependencies are set up, Odoo can be launched by running odoo-bin, the command-line interface of the server. It is located at the root of the Odoo Community directory.
```
Python3 odoo-bin -c debian/odoo.conf
```

In you browser access odoo through
```
localhost:8069
```

<h3>Author</h3>
<h4>Ruben de Pina</h4>
<p><div>
    <a href = "mailto:rubenpina758@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
   <a href="https://www.linkedin.com/in/ruben-pina-3851b4235/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div></p>
