#!/usr/local/bin/python3
# vim setup:
    # setlocal foldmethod=indent
    # highlight Folded ctermbg=NONE
    # set foldtext = '++'
    # set foldignore = ''

"""
Generate an html file for my portfolio site.
    Pull text and links from /projects.csv
    `git pull` all listed repos
    Pull images and data from local (updated) repos etc.
    (Over)Write the html file
    (Over)Write the images and data
    """

def complete(html=''): 
    x = f"""
    <!DOCTYPE html>
    <html>
    {html}
    </html>
    """
    return x
def html(head='', body=''):
    x = f"""<head>
    {head}
    </head>
    <body>
    {body}
    </body>
    """
    return x
def head(title=''):
    x = f"""
    <title>{title}</title>
    <link type="text/css" rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" href="styles.css">
    """
    return x
def title(maintitle='', subtitle=''):
    if subtitle:
        x = f"{main_title}: {subtitle}"
    else:
        x = main_title
    return x
def headers(maintitle='', subtitle=''):
    x = f"""
    <h1 style="text-align:center">{maintitle}</h1>
    <h3 style="text-align:center">{subtitle}</h3>
    """
    return x
def body(headers='', content='', footers=''):
    x = f"""
    {headers}
    <br>
    {content}
    <br>
    {footers}
    """
    return x
def content():
    x = f"""
    <div class="d-flex justify-content-center">
    <table width="90%">
        <tr>
          <th width="50%" class="ps-4">
            <h3>                                                    rongzi
            </h3>
          </th>
          <th rowspan="2" style="text-align: center;" class="p-2">
            <img src=                                               "img/paths2.png" 
                 style="height:15em">
          </th>
        </tr>
        <tr>
          <td width="50%" class="p-2">
            <p><i>                          Find optimal network paths connecting Chinese characters 
                                            based on shared components
            </i></p>
            <ul>
              <li>webapp: <a href=          "https://rongzi.bhrdwj.net"
                >                           rongzi.bhrdwj.net
                </a></li>
              <li>github: <a href=          "https://github.com/bhrdj/rongzi"
                >                           github.com/bhrdwj/rongzi
                </a></li>
            </ul>
          </td>
        </tr>
      </table>
    </div>

    <br><br>


    <div class="d-flex justify-content-center">
      <table width="90%">
        <tr>
          <th class="ps-4">
            <h3>                                                    predwikt
            </h3>
          </th>
          <th rowspan="2" style="text-align: center;" class="p-2">
            <img src=                                               "img/predwikt.png" 
                 style="height:15em">
          </th>
        </tr>
        <tr>
          <td width="50%" class="p-2">
            <p><i>                          Forecast wikipedia traffic based on wikipedia 
                                            dumps converted into time series.
            </i></p>
            <ul>
              <li>webapp: <a href=          "https://predwikt.bhrdwj.net"
                >                           predwikt.bhrdwj.net
                </a></li>
              <li>github: <a href=          "https://github.com/bhrdj/predwikt"
                >                           github.com/bhrdwj/predwikt
                </a></li>
            </ul>
          </td>
        </tr>
      </table>
    </div>

    <br><br>

    <div class="d-flex justify-content-center">
      <table width="90%">
        <tr>
          <th class="ps-4">
            <h3>                                                    tunasoma
            </h3>
          </th>
          <th rowspan="2" class="p-2"
              style="text-align: center; height: 15em;">
            
            <img src=                                               "img/tunasoma.jpg" 
                 class="mh-100">
          </th>
        </tr>
        <tr>
          <td width="50%" class="p-2">
            <p><i>                          Prototype: Wearable app leveraging speech-to-text for earlier toddler reading.
            </i></p>
            <ul>
              <li>4min video presentation: <a href=          "https://tunasoma.bhrdwj.net"
                >                           tunasoma.bhrdwj.net
                </a></li>
            </ul>
          </td>
        </tr>
      </table>
    </div>
    <br><br>
    """
    return x
# def generate():
#     functions = {i.__name__:i for i in 
#          [complete, html, head, title, headers, body, content]}
#     values = {}
#     for i in functions:
#         values[i] = functions[i]()



# some code i will use afterwards
maintitle = "Steven Bhardwaj"
subtitle = "Full-Stack Data Science"




