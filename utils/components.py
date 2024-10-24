#footer

footer_style = f"""
    <style>
        MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        footer:after {{ 
            visibility: visible;
            display: block;
            position: relative;
            # background-color: red;
            padding: 5px;
            top: 2px;
        }}
    </style>
"""

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """

icons = """<style>
        img {
            max-width: 100%;
        
        }
        
        .headerStyle {
            transition: transform .2s;
        }
        
        .headerStyle:hover {
            
             transform: scale(1.5);
            transition: 0.2s;
        }
        .image1 { 
            padding: 10px;
             transition: transform .2s;
        }
        .image2 
        { 
            padding: 10px;
             transition: transform .2s;
        }
        .image1:hover {  
            ##border: 4px solid green;
            ##border-radius: 15px;
             transform: scale(1.5);
            transition: 0.2s;
        }

        .image2:hover {  
            ##border: 4px solid green;
            ##border-radius: 15px;
             transform: scale(1.5);
            transition: 0.2s;
        }
        
        a:link,
        a:visited {
            color: blue;
            background-color: transparent;
            text-decoration: underline;
        }

        a2:hover {
            border-style: solid;
            },
        a:active {
            color: red;
            background-color: transparent;
            text-decoration: underline;
        }
    
        .footer {
            position: fixed;
            width: 100%;
            background-color: white;
            color: black;
            display: block;
            text-align: center;
            padding: 100px;
            top: 0px;
        }
</style>
"""

footer = """<style>
img {
            max-width: 100%;
        
        }
        
        .headerStyle {
            transition: transform .2s;
        }
        
        .headerStyle:hover {
            
             transform: scale(1.5);
            transition: 0.2s;
        }
        .image1 { 
            padding: 10px;
             transition: transform .2s;
        }
        .image2 
        { 
            padding: 10px;
            width: auto;
             transition: transform .2s;
        }
        .image1:hover {  
            ##border: 4px solid green;
            ##border-radius: 15px;
             transform: scale(1.5);
            transition: 0.2s;
        }

        .image2:hover {  
            ##border: 4px solid green;
            ##border-radius: 15px;
             transform: scale(1.5);
            transition: 0.2s;
        }
        
        a:link,
        a:visited {
            color: blue;
            background-color: transparent;
            text-decoration: underline;
        }

        a2:hover {
            border-style: solid;
            },
        a:active {
            color: red;
            background-color: transparent;
            text-decoration: underline;
        }
.footer {
position: relative;
width: 100%;
left: 0;
bottom: 0;
background-color: transparent;
margin-top: auto;
color: #163172;
padding: 24px;
text-align: center;
}
</style>
<div class="footer">
<p style="font-size:  13px">TRG International</p>
<p style="font-size: 13px">This software is distributed under an MIT licence. Please consult the LICENSE file for more details.</p>
<a href="https://aws.amazon.com/vi/free/?trk=a1f96d77-24e3-497e-b5fc-bab658afe631&sc_channel=ps&ef_id=:G:s&s_kwcid=AL!4422!10!72018238917871!72018763037108&msclkid=d328557ca6871921754832655a01ce33">
    <img class="image2" src="https://download.logo.wine/logo/Amazon_Web_Services/Amazon_Web_Services-Logo.wine.png" alt="AWS" width="70" height="70">
</a>
<a href="https://www.infor.com/en-sg">
    <img class="image2" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/infor_logo_icon_167926.png" alt="Infor" width="100" height="70">
</a>
<a href="https://www.trginternational.com">
    <img class="image2" src="https://itviec.com/rails/active_storage/representations/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBM29zREE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--616d9d3a169cb82bd3a282487b2a9fed671505c7/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--15c3f2f3e11927673ae52b71712c1f66a7a1b7bd/trg-international-logo.png" alt="TRG" width="70" height="70">
</a>
<a href="https://github.com/Bell1609/SOP-Request-Server.git">
    <img class="image2" src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="70" height="70">
</a>

"""

color_style = """
    <style>
    :root {
      --primary-color: blue;
    }
    </style>
"""
