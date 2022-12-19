# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 17:07
# @Author  : crab-pc
# @File    : revistas_usta1214.py
import re
from urllib.parse import urljoin
from Yjsdl import Spider, item
import requests


html = """
<!DOCTYPE html>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<html lang="es-ES" xml:lang="es-ES">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Revistas Universidad Santo Tomás - Colombia
					</title>
        <meta name="generator" content="Open Journal Systems 3.3.0.10">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css?v=3.3.0.10" type="text/css"/>
        <link rel="stylesheet" href="https://revistas.usantotomas.edu.co/plugins/themes/responsive/css/newtheme.css?v=3.3.0.10" type="text/css"/>
        <link rel="stylesheet" href="https://revistas.usantotomas.edu.co/plugins/themes/responsive/css/responsive.css?v=3.3.0.10" type="text/css"/>
        <link rel="stylesheet" href="https://revistas.usantotomas.edu.co/index.php/index/$$$call$$$/page/page/css?name=stylesheet" type="text/css"/>
        <link rel="stylesheet" href="https://revistas.usantotomas.edu.co/plugins/generic/orcidProfile/css/orcidProfile.css?v=3.3.0.10" type="text/css"/>
    </head>
    <body class="pkp_page_index pkp_op_index has_site_logo">
        <div class="pkp_structure_page">
            <nav id="accessibility-nav" class="sr-only" role="navigation" aria-labelled-by="accessible-menu-label">
                <h2 id="accessible-menu-label">Salto rápido al contenido de la página
			</h2>
                <ul>
                    <li>
                        <a href="#main-navigation">Navegación principal</a>
                    </li>
                    <li>
                        <a href="#main-content">Contenido principal</a>
                    </li>
                    <li>
                        <a href="#sidebar">Barra lateral</a>
                    </li>
                </ul>
            </nav>
            <header class="navbar navbar-default" id="headerNavigationContainer" role="banner">
                <div class="topHeader">
                    <div class="container">
                        <div class="row">
                            <div class="topSocial">
                                <!-- CONFIGURAR EL VINCULO DE LAS REDES SOCIALES -->
                                <ul>
                                    <li>
                                        <a href="https://www.facebook.com/EdicionesUSTA/" class="fa fa-facebook" target="_blank"></a>
                                    </li>
                                    <li>
                                        <a href="https://twitter.com/EdicionesUSTA" class="fa fa-twitter" target="_blank"></a>
                                    </li>
                                    <li>
                                        <a href="https://co.linkedin.com/in/ediciones-usta-08a011bb" class="fa fa-linkedin" target="_blank"></a>
                                    </li>
                                    <li>
                                        <a href="https://www.youtube.com/user/EdicionesUSTA" class="fa fa-youtube" target="_blank"></a>
                                    </li>
                                    <li>
                                        <a href="https://www.instagram.com/edicionesusta/" class="fa fa-instagram" target="_blank"></a>
                                    </li>
                                </ul>
                            </div>
                            <div id="social-icons" class="pull-right">
                                <ul class="menu">
                                    <li>
                                        <a href="/">
                                            <i class="fa fa-university" aria-hidden="true"></i>
                                            Inicio Revistas
                                        </a>
                                    </li>
                                    <li class="newDropDown languages" aria-haspopup="true" aria-expanded="false">
                                        <a href="javascript:void(0)" class="">
                                            <span class="fa fa-globe"></span>
                                            Español (España)
                                        </a>
                                        <ul id="navigationUser" role="navigation" aria-label="Navegación del usuario">
                                            <li>
                                                <a href="https://revistas.usantotomas.edu.co/index.php/index/user/setLocale/en_US?source=%2F">English
													</a>
                                            </li>
                                            <li>
                                                <a href="https://revistas.usantotomas.edu.co/index.php/index/user/setLocale/fr_CA?source=%2F">Français (Canada)
													</a>
                                            </li>
                                            <li>
                                                <a href="https://revistas.usantotomas.edu.co/index.php/index/user/setLocale/fr_FR?source=%2F">Français (France)
													</a>
                                            </li>
                                            <li>
                                                <a href="https://revistas.usantotomas.edu.co/index.php/index/user/setLocale/pt_BR?source=%2F">Português (Brasil)
													</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="https://revistas.usantotomas.edu.co/index.php/index/user/register">
                                            <i class="fa fa-key"></i>
                                            Registrarse
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://revistas.usantotomas.edu.co/index.php/index/login">
                                            <i class="fa fa-user"></i>
                                            Entrar
                                        </a>
                                    </li>
                                </ul>
                                <div class="clearfix"></div>
                            </div>
                        </div>
                        <!-- .row -->
                    </div>
                    <!-- .container-fluid -->
                </div>
                <div class="mainNavigation">
                    <div class="container ">
                        <div class="navbar-header" style="height:110px">
                            <!-- CONFIGURAR EL ALTO DE LA POSICION DONDE ESTA EL LOGO DE LAS REVISTAS -->
                            <!-- <h1 class="site-name"> -->
                            <div class="site-name">
                                <!-- <a href="https://revistas.usantotomas.edu.co/index.php/index/index" class="navbar-brand navbar-brand-logo"> LINEA ORIGINAL DEL VINCULO DEL LOGO DE LAS REVISTAS QUE LLEVA AL SITIO PRINCIPAL -->
                                <a href="https://revistas.usantotomas.edu.co/index.php/index/index" class="navbar-brand navbar-brand-logo">
                                    <img src="https://revistas.usantotomas.edu.co/public/site/pageHeaderTitleImage_es_ES.png" class="img-responsive" alt="Open Journal Systems" title="Open Journal Systems"/>
                                </a>
                                <!-- </h1> -->
                            </div>
                        </div>
                    </div>
                </div>
                <div class="thirdHeader hideOnMobile"></div>
                <!-- .pkp_head_wrapper -->
            </header>
            <!-- .pkp_structure_head -->
            <div class="pkp_structure_content container" id="mainContainer">
                <main class="pkp_structure_main col-md-9" role="main">
                    <div id="main-site" class="page_index_site">
                        <!--	Linea Original <h2 class="current_issue_title lead text-center" style="padding:6px; margin: 0 0 1em 0;letter-spacing: 1px;text-transform: uppercase;">  Open <span class="Jmiddle" style="color:#ee3733">Journal </span>systems publishing   </h2> -->
                        <h2 class="current_issue_title lead text-center" style="padding:6px; margin: 0 0 1em 0;letter-spacing: 1px;text-transform: uppercase;">
                            Revistas acad &eacute;micas y cient &iacute;ficas <span class="Jmiddle" style="color:#ee3733"></span>
                        </h2>
                        <div class="journals">
                            <!-- <div class="page-header">
			<h2>
				##journal.journals##
			</h2>
		</div> -->
                            <ul class="media-list">
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/activos">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/21/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/activos" rel="bookmark">Revista Activos
								</a>
                                        </h3>
                                        <div class="description">
                                            <p>El objetivo principal de la revista es visibilizar conocimiento científico en materia contable, a nivel nacional e internacional. Publica artículos de reflexión, análisis y resultados de investigación alrededor de la disciplina y la profesión contable. La Revista Activos ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/activos">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/activos/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/activos/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/albertus-magnus">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/20/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/albertus-magnus" rel="bookmark">Revista Albertus Magnus
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Revista editada desde el 2003 dentro del espacio del Studium Generale en el Convento Santo Domingo de Colombia. Se presenta como un espacio de divulgación del conocimiento teológico e interdisciplinar, contemplando la realidad y lo que ella aporte al acercami ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/albertus-magnus">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/albertus-magnus/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/albertus-magnus/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/analisis">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/4/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/analisis" rel="bookmark">Análisis
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">La revista Análisis es un órgano de difusión de resultados de investigaciones en el campo de las humanidades, las ciencias sociales y la filosofía; así como de trabajos que emerjan del diálogo de las disciplinas humanísticas con los demás saberes y la c ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/analisis">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/analisis/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/analisis/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/campos">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/17/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/campos" rel="bookmark">Campos en Ciencias Sociales
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">
                                                La revista &nbsp;
                                                <em>
                                                    Campos en Ciencias Sociales<strong>&nbsp;</strong>
                                                </em>
                                                es una publicación interdisciplinar en ciencias sociales, de carácter científico e investigativo, que nace en el año 2013 y tiene como objetivo ofrecer a la comunidad académica un e ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/campos">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/campos/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/campos/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/cfla">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/11/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/cfla" rel="bookmark">Cuadernos de Filosofía Latinoamericana
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Publicación científica editada por primera vez en el año 1979, está dirigida a investigadores, intelectuales, profesores y estudiantes interesados en el devenir filosófico en Colombia y América Latina. Su objetivo es fomentar el cultivo de la filosofía e ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/cfla">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/cfla/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/cfla/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/rccm">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/16/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/rccm" rel="bookmark">Cuerpo, Cultura y Movimiento
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Esta revista, editada desde el 2011, fomenta la construcción y difusión de nuevo conocimiento en las áreas de la cultura física, el deporte y la recreación a niveles nacional e internacional, y se constituye en un nuevo espacio de discusión y desarrollo h ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/rccm">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/rccm/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/rccm/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/hallazgos">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/12/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/hallazgos" rel="bookmark">Hallazgos
								</a>
                                        </h3>
                                        <div class="description">
                                            <p>Revista internacional especializada en Ciencias Sociales y Humanidades, y las disciplinas propias de estas áreas del conocimiento, se enfoca principalmente a las dinámicas propias de América Latina en diálogo con otras realidades mundiales. Cuenta con 17 años de edición  ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/hallazgos">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/hallazgos/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/hallazgos/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/iusta">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/13/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/iusta" rel="bookmark">IUSTA
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Publicación fundada en el año 2004. La política editorial de la revista ha sido recoger trabajos de los profesores de la Facultad de Derecho y colaboraciones externas que se refieran a un campo específico del saber jurídico para ampliar las fronteras de co ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/iusta">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/iusta/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/iusta/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/cife">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/15/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/cife" rel="bookmark">Revista CIFE: Lecturas de Economía Social
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Revista editada desde 1998, auspicia y difunde el quehacer académico y la investigación en el área de las ciencias económicas en articulación con otras disciplinas del ámbito de las ciencias humanas y exactas para avanzar hacía la economía social. Asume ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/cife">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/cife/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/cife/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/signos">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/18/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/signos" rel="bookmark">SIGNOS - Investigación en sistemas de gestión
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Publicación resultado del convenio entre el Icontec y la División de Ingeniería de la Universidad Santo Tomás. Tiene como propósito divulgar las reflexiones, la discusión y los resultados de investigación en temas relacionados con la calidad y su gestió ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/signos">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/signos/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/signos/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/viei">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/19/journalThumbnail_es_ES.jpg">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/viei" rel="bookmark">Via Inveniendi Et Iudicandi
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Publicación virtual destinada a la difusión de la producción académica de investigadores tomasinos e invitados, docentes y estudiantes adscritos a investigaciones institucionales, formativas y semilleros de investigación de la Facultad de Derecho de la Uni ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/viei">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/viei/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/viei/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/citas">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/23/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/citas" rel="bookmark">CITAS
								</a>
                                        </h3>
                                        <div class="description">
                                            <p>La revista CITAS, de la Facultad de Ciencias y Tecnologías de la División de Educación Abierta y a Distancia, tiene como objetivo: (1)&nbsp;presentar los avances y resultados de trabajos de investigación relacionados con ciencia, innovación, tecnología, ambiente y socied ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/citas">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/citas/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/citas/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/soldeaquino">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/26/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/soldeaquino" rel="bookmark">Sol de Aquino
								</a>
                                        </h3>
                                        <div class="description">
                                            <p>Es una publicación interdisciplinar de carácter institucional y divulgativo, que nace en el año 2003 y tiene como propósito visibilizar ante la comunidad tomasina y la población en general, las experiencias derivadas de las actividades universitarias de la USTA y ligadas  ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/soldeaquino">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/soldeaquino/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/soldeaquino/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/diversitas">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/3/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/diversitas" rel="bookmark">Diversitas
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Publicación científica, semestral, editada desde el 2005. Tiene como propósito la divulgación del trabajo científico e investigativo de la Psicología, de variados ejes temáticos, teóricos y metodológicos, permitiendo el intercambio y la transferencia d ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/diversitas">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/diversitas/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/diversitas/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/estadistica">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/1/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/estadistica" rel="bookmark">Comunicaciones en Estadística
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">Revista editada desde el 2008 con el objetivo de divulgar artículos originales e inéditos en cualquier temática de la estadística teórica y/o aplicada. La finalidad de la revista es motivar la cultura de la investigación estadística y por ende su públic ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/estadistica">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/estadistica/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/estadistica/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/episteme">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/22/journalThumbnail_es_ES.jpg">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/episteme" rel="bookmark">Episteme. Revista de Estudios Socioterritoriales
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">
                                                <em>EPISTEME. Revista de Estudios Socioterritoriales </em>
                                                es la publicación de divulgación científica, de acceso abierto, de la Universidad Santo Tomás - Sede Villavicencio (Colombia). Fundada en 2010, la revista publica trabajos inéditos de profesionales, ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/episteme">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/episteme/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/episteme/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/artefacto">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/25/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/artefacto" rel="bookmark">Arte-Facto: Revista de estudiantes de Humanidades
								</a>
                                        </h3>
                                        <div class="description">
                                            <p>
                                                Al hacer referencia al término &nbsp;<strong>“artefacto”</strong>
                                                &nbsp;vienen a nuestra mente la relación que se establece con máquinas o instrumentos que facilitan algunas tareas cotidianas del ser humano. Sin embargo, nosotros nos remontamos un poco más atrás en la h ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/artefacto">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/artefacto/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/artefacto/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/riiep">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/2/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/riiep" rel="bookmark">Revista Interamericana de Investigación Educación y Pedagogía RIIEP
								</a>
                                        </h3>
                                        <div class="description">
                                            <p>La Revista Interamericana de Investigación, Educación y Pedagogía (RIIEP) es una publicación adscrita a la Vicerrectoría Académica de la Universidad Santo Tomás en coedición con la Vicerrectoría de Investigación de la Universidad Nacional Abierta y a Distancia (UNAD) ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/riiep">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/riiep/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/riiep/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/aquinas">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/27/journalThumbnail_es_ES.png">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/aquinas" rel="bookmark">Aquinas 'Scriptum Scientiam'
								</a>
                                        </h3>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/aquinas">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/aquinas/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/aquinas/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="media  col-md-6">
                                    <div class="media-left">
                                        <a href="https://revistas.usantotomas.edu.co/index.php/magistro">
                                            <img class="media-object" src="https://revistas.usantotomas.edu.co/public/journals/10/journalThumbnail_es_ES.jpg">
                                        </a>
                                    </div>
                                    <div class="media-body">
                                        <h3 class="media-heading">
                                            <a href="https://revistas.usantotomas.edu.co/index.php/magistro" rel="bookmark">Magistro
								</a>
                                        </h3>
                                        <div class="description">
                                            <p align="justify">
                                                La revista <em>Magistro</em>
                                                (ISSN: 2011-8643 | e-ISSN: 2500-543X) se complace en informar a sus lectores que, siguiendo la política editorial de la VUAD, se ha fusionado con la <a href="https://revistas.usantotomas.edu.co/index.php/riiep">Revista Interamerica ...
									
								
                                        </div>
                                        <ul class="nav nav-pills">
                                            <li class="view">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/magistro">Ver revista
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/magistro/issue/current">Número actual 
									</a>
                                            </li>
                                            <li class="current">
                                                <a href="https://revistas.usantotomas.edu.co/index.php/magistro/about/submissions">Envíos</a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <!-- .page -->
                    <style>
                        .pkp_structure_main {
                            border-right: 0px solid #dddddd;
                        }

                        .pkp_structure_main.col-md-9 {
                            width: 100%;
                        }
                    </style>
                </main>
            </div>
            <!-- pkp_structure_content -->
            <link href="/var/www/html/revistas_ustacolombia/plugins/themes/responsive/font-awesome/css/font-awesome.css" rel="stylesheet">
            <div class="footerSupports">
                <a href="https://www.openaccess.nl/en" target="_blank">
                    <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/Open_Access.jpg.png">
                </a>
                <!-- <a href="https://doaj.org/" target="_blank"><img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/cropped-doaj_logo_big.png"></a> -->
                <!-- <a href="https://www.ncbi.nlm.nih.gov/pubmed/" target="_blank""><img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/Pubmed-logo.png"></a> -->
                <a href="https://search.crossref.org/" target="_blank">
                    <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/crossref-logo-landscape-200.png">
                </a>
                <a href="https://orcid.org/" target="_blank">
                    <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/orcid_logo.png">
                </a>
                <a href="https://publicationethics.org/" target="_blank">
                    <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/Cope_logo_3.png">
                </a>
                <a href="https://creativecommons.org/" target="_blank">
                    <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/cc.logo.large.png">
                </a>
            </div>
            <footer id="footer" class="footer" role="contentinfo">
                <div class="container">
                    <div class="row footer-widgets">
                        <!-- Start Contact & Follow Widget -->
                        <div class="col-md-4 col-xs-12">
                            <div class="footer-widget contact-widget">
                                <h4>
                                    <a href="" alt="Footer Logo" ss="">
                                        <!-- <img src="https://revistas.usantotomas.edu.co/public/site/pageHeaderTitleImage_es_ES.png" alt="R" class="img-responsive"> -->
                                        <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/Cabezotes-sin-fondo.png" class="img-responsive">
                                        <p></p>
                                        <img src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/img/conmemoracion.png" width="80%" height="80%" style="padding-left:15%" class="img-responsive">
                                    </a>
                                </h4>
                                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultrices lorem et lacinia consequat. Donec tristique finibus iaculis. Nulla sit amet justo commodo, pellentesque elit eget, varius enim. Sed enim odio, venenatis a ultricies vel, ullamcorper quis justo. Quisque porttitor risus in vehicula vestibulum. In in eros tempor, blandit erat eu, suscipit mauris. Aliquam facilisis, eros eget fermentum efficitur, justo metus varius mi, nec aliquet augue leo at arcu.
              
              </p>
              <ul>
                <li><span class="fa fa-">ISSN</span> 2466-3352 (Online)</li>
              </ul> -->
                            </div>
                        </div>
                        <!-- .col-md-6 -->
                        <!-- End Contact Widget -->
                        <div class="footer-widget col-md-3 col-xs-12 social-widget">
                            <h4>
                                ContactO<span class="head-line"></span>
                            </h4>
                            <p></p>
                            <ul>
                                <!-- CONFIGURAR INFORMACI�N DEL PIE DE PAGINA -->
                                <li>
                                    <span class="fa fa-envelope"></span>
                                    Correo electr &oacute;nico: editorial@usantotomas.edu.co 
                                </li>
                                <li>
                                    <span class="fa fa-phone"></span>
                                    Tel &eacute;fono: (571) 587 87 97 Ext. 2991
                                </li>
                                <li>
                                    <span class="fa fa-globe"></span>
                                    Website: www.usta.edu.co
                                </li>
                                <li>
                                    <span class="fa fa-map-marker"></span>
                                    Direcci &oacute;n: Carrera 9 # 51-11, Bogot &aacute;D. C.
</br>Sede Principal, Edificio Lu &iacute;s J. Torres, S &oacute;tano 1 </li></ul>
<ul class="social-icons">
    <!-- CONFIGURAR EL VINCULO DE LAS REDES SOCIALES -->
    <li>
        <a class="facebook" href="https://www.facebook.com/EdicionesUSTA/" target="_blank">
            <span class="fa fa-facebook"></span>
        </a>
    </li>
    <li>
        <a class="twitter" href="https://twitter.com/EdicionesUSTA" target="_blank">
            <span class="fa fa-twitter"></span>
        </a>
    </li>
    <li>
    <!--    <a class="google" href="https://plus.google.com/+Openjournalsystems" target="_blank"><span class="fa fa-google-plus"></span></a> -->
    </li>
    <li>
        <a class="linkdin" href="https://co.linkedin.com/in/ediciones-usta-08a011bb" target="_blank">
            <span class="fa fa-linkedin"></span>
        </a>
    </li>
    <li>
        <a class="linkdin" href="https://www.youtube.com/user/EdicionesUSTA" target="_blank">
            <span class="fa fa-youtube"></span>
        </a>
    </li>
    <li>
        <a class="linkdin" href="https://www.instagram.com/edicionesusta/" target="_blank">
            <span class="fa fa-instagram"></span>
        </a>
    </li>
</ul>
</div>
<div class="footer-widget col-md-2 col-xs-12 social-widget">
    <h4>
        Otras Revistas USTA<span class="head-line"></span>
    </h4>
    <ul>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/ITECKNE/index" target="_blank">Iteckne</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustatunja.edu.co/index.php/ingeniomagno" target="_blank">Ingenio Magno</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustatunja.edu.co/index.php/qdisputatae" target="_blank">Quaestiones Disputatae</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/TEMAS/index" target="_blank">Temas</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="https://revistas.usantotomas.edu.co/index.php/basicamente" target="_blank">B &aacute;sicamente</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustatunja.edu.co/index.php/ivestigium" target="_blank">In Vestigium Ire</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/LEBRET" target="_blank">Lebret</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustatunja.edu.co/index.php/piuris" target="_blank">Principia Iuris</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/IUSTITIA" target="_blank">Iustitia</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/ESPIRAL" target="_blank">Espiral</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/USTASALUD_ODONTOLOGIA/index" target="_blank">UstaSalud</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="http://revistas.ustabuca.edu.co/index.php/REVISTAM" target="_blank">Revista M</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="https://revistas.usantotomas.edu.co/index.php/magistro/index" target="_blank">Magistro</a>
        </li>
        <li>
            <span class="fa fa-dot-circle-o"></span>
            <a title="Information For Readers" href="https://revistas.usantotomas.edu.co/index.php/aquinas/index" target="_blank">Aquin@s</a>
        </li>
    </ul>
</div>
<!-- Start Twitter Widget -->
<div class="col-md-3 col-xs-12">
    <div class="footer-widget twitter-widget">
        <h4>
            Ediciones USTA<span class="head-line"></span>
        </h4>
        <!-- CONFIGURAR LA VENTANA DONDE SE PUBLICAN LOS TwEETS Y SUS RESPUETAS -->
        <a class="twitter-timeline" href="https://twitter.com/EdicionesUSTA" data-widget-id="494122051230121986">Tweets by @OpenJournalSys</a>
        <script>
            !function(d, s, id) {
                var js, fjs = d.getElementsByTagName(s)[0], p = /^http:/.test(d.location) ? 'http' : 'https';
                if (!d.getElementById(id)) {
                    js = d.createElement(s);
                    js.id = id;
                    js.src = p + "://platform.twitter.com/widgets.js";
                    fjs.parentNode.insertBefore(js, fjs);
                }
            }(document, "script", "twitter-wjs");
        </script>
    </div>
</div>
<!-- .col-md-3 -->
<!-- End Twitter Widget -->
<!-- Start Subscribe Widget -->
<!-- .col-md-3 -->
<!-- End Subscribe Widget -->
</div>
<!-- .row -->
<!-- Start Copyright -->
<div class="copyright-section">
    <div class="row">
        <style type="text/css">
            footer {
                background: #444;
                color: #fff;
            }

            .footer .bottom-bar {
                padding: 5px 0;
            }

            footer img {
                margin: 5px;
            }

            #nsf-logo {
                margin-left: 25px;
                margin-right: 25px;
            }

            .cu-engineering-logo {
                width: 160px;
            }
        </style>
        <!-- <div class="bottom-bar">
    <div class="container text-center ">
        <div class="row">
            <a href="/">Home</a> | <a href="">FAQs</a> | <a href="">Policies</a> | <a href="">Contact Us</a> | <a href="">Sponsors</a> | <a href="">Sitemap</a>
            <div>
                Use of this website constitutes acceptance of our <a href="">Terms of Use</a> and <a href="">Privacy Policy</a>
            </div>
        </div>
        
        <div class="row">
            
        <div class="small">
           Ediciones USTA, </br>
Universidad Santo Tom&aacute;s OJS Hosting, Support, and Customization by: <a href="http://OpenJournalSystems.com">OpenJournalSystems.com</a>
        </div>

        </div>
    </div>
</div> -->
    </div>
    <!-- .row -->
</div>
<!-- End Copyright -->
</div>
<!-- .container -->
</footer></div>
<!-- pkp_structure_page -->
<script src="https://code.jquery.com/jquery-3.6.1.js?v=3.3.0.10" type="text/javascript"></script>
<script src="https://code.jquery.com/ui/1.13.2/jquery-ui.js?v=3.3.0.10" type="text/javascript"></script>
<script src="https://revistas.usantotomas.edu.co/lib/pkp/js/lib/jquery/plugins/jquery.tag-it.js?v=3.3.0.10" type="text/javascript"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js?v=3.3.0.10" type="text/javascript"></script>
<script src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/js/article.js?v=3.3.0.10" type="text/javascript"></script>
<script src="https://revistas.usantotomas.edu.co/plugins/themes/responsive/js/main.js?v=3.3.0.10" type="text/javascript"></script>
<script src="https://www.google.com/recaptcha/api.js?v=3.3.0.10" type="text/javascript"></script>
<script type="text/javascript">
    $(function() {
        var baseUrl = window.location;
        //alert(baseUrl)
        $('#main-navigation a[href="' + baseUrl + '"]').addClass('active');

        $('body').on('click', '.show-search', function(e) {
            var flag = $('#seachCheckFlag').prop('checked');

            if (flag == true) {
                $('#seachCheckFlag').prop('checked', false);
                // if( $('#searchWrpNav form input').val()!=''){
                setTimeout(function() {
                    $('#searchWrpNav button[type="submit"]').click();
                }, 1000);
                // }
            } else {
                $('#seachCheckFlag').prop('checked', true);
            }

        });

        //slider
        function makeSlider(id) {
            var images = '';
            var Icount = 0;
            $(id + ' img').each(function(i) {
                Icount++;
                var activeClass = "";
                if (i == 0) {
                    activeClass = "active";
                }

                images += '<div class="item ' + activeClass + '">\
                              <img src="' + $(this).attr('src') + '"/>\
                            </div>';
            });
            if (Icount == 0)
                return;

            var slidertemplate = '<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\
                              <!-- Indicators -->\
                              <ol class="carousel-indicators">\
                                <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\
                                <li data-target="#carousel-example-generic" data-slide-to="1"></li>\
                                <li data-target="#carousel-example-generic" data-slide-to="2"></li>\
                              </ol>\
                              <!-- Wrapper for slides -->\
                              <div class="carousel-inner" role="listbox">\
                                ' + images + '\
                              </div>\
                              <!-- Controls -->\
                              <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">\
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\
                                <span class="sr-only">Previous</span>\
                              </a>\
                              <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">\
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\
                                <span class="sr-only">Next</span>\
                              </a>\
                            </div>';
            $(id).html(slidertemplate);
            $('.carousel').carousel();

        }

        makeSlider('#customblock-Slider');

    });
</script>
</body></html>

"""

class RevistasUsta1214(Spider):
    request_config = {
        "RETRIES": 3,
        "DELAY": 0,
        "TIMEOUT": 20
    }
    # 并发
    concurrency = 2

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'accept-encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    async def start_requests(self):
        yield self.request(
            url='https://revistas.usantotomas.edu.co/',
            headers=self.headers.copy(),
        )

    async def parse(self, response):
        # html = await response.text()
        res = response.html_etree(html=html)
        lists = res.xpath('//ul[@class="media-list"]/li')
        for one in lists:
            name = one.xpath('.//div/h3/a/text()')[0].replace('\t', '').replace('\n', '')
            url = one.xpath('.//div/h3/a/@href')[0]
            pic = one.xpath('.//div/a/img/@src')[0]
            meta = dict(name=name, url=url, pic=pic)
            yield self.request(
                url=url,
                headers=self.headers.copy(),
                meta= meta,
                callback=self.details_parse
            )

    async def details_parse(self, response):
        meta= response.meta

        html = requests.get(url=meta['url'], headers=self.headers.copy()).text
        # html = await response.text()
        res = response.html_etree(html=html)
        issns = res.xpath('//div[@class="journal-description"]/p//text()')


        issns = ''.join(issns)
        issn = re.findall('\d+-\d+', issns)
        issns_dict = {f'issn{index + 1}': v for index, v in enumerate(issn)}
        contribute_link = meta['url'] + '/login'

        data = item.CsvItem(data_storage=r'F:\mysubject\contribute_link\contributuLink\投稿链接',
                            filename='revistas_usta1214')
        data.append(
            dict(title_name=meta['name'], url=meta['url'], pic=meta['pic'], issn1=issns_dict.get('issn1', ''),
                 issn2=issns_dict.get('issn2', ''), contribute_link=contribute_link))
        yield data


if __name__ == '__main__':
    RevistasUsta1214.start()
