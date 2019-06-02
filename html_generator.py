import os 

if __name__ == '__main__':
    html_auto_file = open('auto.html', 'w')  
    src_name = "projects"

    for dir_name in os.listdir(src_name):
        if os.path.isdir(src_name + '/' + dir_name):
            number = len(os.listdir(src_name + '/' + dir_name))

            if os.path.exists(src_name + '/' + dir_name + '/' + '.DS_Store'):
                os.remove(src_name + '/' + dir_name + '/' + '.DS_Store')

            if number is not 4:
                print("Warning: There should be 4 files in {} but {} found".format(src_name + '/' + dir_name, number))
            else:
                print("Generate html code for files in {}".format(src_name + '/' + dir_name))

                for file_name in os.listdir(src_name + '/' + dir_name):
                    if 'poster' in file_name or 'Poster' in file_name:
                        poster_name = file_name
                    elif 'project' in file_name or 'Project' in file_name:
                        report_name = file_name
                    elif '.png' in file_name:
                        logo_name = file_name
                    elif file_name == 'info':
                        info_name = file_name
                    else:
                        raise Exception('Unknown file {} in directory {}'.format(file_name, dir_name))
                
                info_file = open(src_name + '/' + dir_name + '/' + info_name, 'r')
                title_name = info_file.readline().strip('\n')
                author_name = info_file.readline().strip('\n') 

                html_code = '<div class="project-item">\n' \
                            +'<div class="project-preview">\n' \
                            +'<img src="' + src_name + '/' + dir_name + '/' + logo_name + '"></div>\n' \
                            +'<div class="project-desc">\n' \
                            +'<p class="project-title">' + title_name + '</p>\n' \
                            +'<p class="project-team">' + author_name + '</p>\n' \
                            +'<p class="project-links">\n' \
                            +'<a href="' + src_name + '/' + dir_name + '/' + report_name + '">[report]</a>&nbsp;\n' \
                            +'<a href="' + src_name + '/' + dir_name + '/' + poster_name + '">[poster]\n' \
                            +'</a></p></div></div>'

                html_auto_file.write(html_code)
                html_auto_file.write('\n\n')

           