# -*- coding: utf-8 -*-
# @Time    : 2022/12/08 16:18
# @Author  : crab-pc
# @File    : annualreviews.py
from urllib.parse import urljoin
import os
import pandas as pd
from Yjsdl import Spider


# class Annualreviews(Spider):
#     request_config = {
#         "RETRIES": 3,
#         "DELAY": 0,
#         "TIMEOUT": 20
#     }
#     # 并发
#     concurrency = 2
#
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#
#     }
#
#     async def start_requests(self):
#         yield self.request(
#             url='https://www.annualreviews.org/action/showPublications',
#             headers=self.headers.copy(),
#         )
#
#     async def parse(self, response):
#         html = await response.text()
#         print(html)
#
#
# if __name__ == '__main__':
#     Annualreviews.start()


# 保存到csv文件
def save_list(data, file, name):
    # desk = os.path.join(os.path.expanduser('~'), 'Desktop')
    # 当前文件夹
    file_path = r'F:\mysubject\contribute_link\contributuLink\投稿链接\\' + file
    if os.path.isfile(file_path):
        df = pd.DataFrame(data=data)
        df.to_csv(file_path, encoding="utf-8", mode='a', header=False, index=False)
    else:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df = pd.DataFrame(data=data, columns=name)
        df.to_csv(file_path, encoding="utf-8", index=False)
text = """





    
    
        
    



    
    
    
    
        <!DOCTYPE html>

<!--[if IE 9]>
<html class="no-js lt-ie10" lang="en"      class="pb-page"  data-request-id="8d161820-4520-40e1-a2cb-1212660a2c29"  
> <![endif]-->

<!--[if (gt IE 9)|!(IE)]><!-->
<html lang="en"     class="pb-page"  data-request-id="8d161820-4520-40e1-a2cb-1212660a2c29"  
><!--<![endif]-->

<head data-pb-dropzone="head"><meta name="pbContext" content=";page:string:Show Publications;wgroup:string:AR Group;website:website:ar-site;subPage:string:Show All"/>


<title>Browse  Journals</title>





<meta charset="UTF-8">
<meta name="robots" content="noarchive,noindex"/>


















    <meta property="og:title" content="Browse Journals | Annual Reviews" />



    
    
        <meta property="og:url" content=""/>
    


    <meta property="og:image" content="http://www.annualreviews.org/pb-assets/assets/images/social-media/AR_Facebook_Share.jpg" />



    <meta property="og:description" content="Annual Reviews is a nonprofit publisher dedicated to synthesizing and integrating knowledge for the progress of science and the benefit of society. Enjoy browsing our highly-cited journals which span the life, medical, physical and social sciences." />



















<link rel="stylesheet" type="text/css" href="/wro/luqm~article-metrics-phase2.css">
        
<link rel="stylesheet" type="text/css" href="/wro/luqm~product.css"><link rel="stylesheet" type="text/css" href="/pb/css/t1669796796000-v1669796796000/default.css" id="pb-css" data-pb-css-id="t1669796796000-v1669796796000/default.css"/>


<script type="text/javascript">
    if (window.location.hash && window.location.hash == '#_=_') {
        window.location.hash = '';
    }
</script>








    
    

    
    
    
        
        
        
    


<script type="text/javascript" src="/wro/luqm~product.js"></script><meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="origin">
<meta name="twitter:card" content="summary_large_image">
<link rel="apple-touch-icon" href="https://www.annualreviews.org/pb-assets/assets/images/icons/apple-touch-icon/apple-touch-icon-1582743354193.png">
<!-- old one <link rel="stylesheet" href="https://s3.amazonaws.com/icomoon.io/55136/AnnualReviews/style.css"> -->
<!-- <link rel="stylesheet" href="https://s3.amazonaws.com/icomoon.io/55136/AnnualReviews/style.css"> -->
<link rel="stylesheet" href="https://d1azc1qln24ryf.cloudfront.net/55136/AnnualReviews/style-cf.css">
<link rel="stylesheet" href="/pb-assets/assets/css/main-1668112995940.css">

<!-- OneTrust Cookies Consent Notice start for annualreviews.org -->
<script type="text/javascript" src="https://cdn.cookielaw.org/consent/dc8545c5-7e20-40b7-9339-972721d7237f/OtAutoBlock.js" ></script>
<script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"  type="text/javascript" charset="UTF-8" data-domain-script="dc8545c5-7e20-40b7-9339-972721d7237f" ></script>
<script type="text/javascript">
function OptanonWrapper() { }
</script>
<!-- OneTrust Cookies Consent Notice end for annualreviews.org -->

<!-- <script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:413175,hjsv:5};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'//static.hotjar.com/c/hotjar-','.js?sv=');
</script> -->
<script src="https://scholar.google.com/scholar_js/casa.js" async></script>

<!-- Hotjar Tracking Code for https://www.annualreviews.org/ -->
<script class="optanon-category-C0002" type="text/plain">
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:1678608,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-1828393-3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-1828393-3');
</script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v652eace1692a40cfa3763df669d7439c1639079717194" integrity="sha512-Gi7xpJR8tSkrpF7aordPZQlW2DLtzUlZcumS8dMQjwDHEnw9I7ZLyiOj/6tZStRBGtGgN6ceN6cMH8z7etPGlw==" data-cf-beacon='{"rayId":"6fb4ca8c7c5df5b9","token":"16f03d22e36d4060b9b3e112eb0bf3d7","version":"2021.12.0","si":100}' crossorigin="anonymous"></script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v652eace1692a40cfa3763df669d7439c1639079717194" integrity="sha512-Gi7xpJR8tSkrpF7aordPZQlW2DLtzUlZcumS8dMQjwDHEnw9I7ZLyiOj/6tZStRBGtGgN6ceN6cMH8z7etPGlw==" data-cf-beacon='{"rayId":"706b5563d9be9855","token":"16f03d22e36d4060b9b3e112eb0bf3d7","version":"2021.12.0","si":100}' crossorigin="anonymous"></script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v652eace1692a40cfa3763df669d7439c1639079717194" integrity="sha512-Gi7xpJR8tSkrpF7aordPZQlW2DLtzUlZcumS8dMQjwDHEnw9I7ZLyiOj/6tZStRBGtGgN6ceN6cMH8z7etPGlw==" data-cf-beacon='{"rayId":"72d59bb01b6a9864","token":"16f03d22e36d4060b9b3e112eb0bf3d7","version":"2022.6.0","si":100}' crossorigin="anonymous"></script>
<!-- Google Tag Manager -->
        <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","url":"","potentialAction":{"@type":"SearchAction","target":"","query-input":"required name=search_term"}}</script>
        <!-- End Google Tag Manager -->
    








    
        
            
            
        
    

<link rel="canonical" href="https://www.annualreviews.org/action/showPublications">
        




</head>
<body class="pb-ui">

<!-- Google Tag Manager -->
            <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KL6C9MW');</script>
            <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KL6C9MW" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
<!-- End Google Tag Manager -->
        



















<script type="text/javascript">

    if(false) {
        document.getElementById("skipNavigationLink").onclick =function skipElement () {
            var element = document.getElementById('');
            if(element == null || element == undefined) {
                element = document.getElementsByClassName('').item(0);
            }
            element.setAttribute('tabindex','0');
            element.focus();

        }

    }

</script>





    <div id="pb-page-content" data-ng-non-bindable>
        <div data-pb-dropzone="main" data-pb-dropzone-name="Main">




    
    
        <div data-widget-def="responsive-layout" data-widget-id="2503ed4d-b8ed-4284-9c15-42ca8f034edb">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 page-container">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="general-html-asset" data-widget-id="015ae563-d1c6-48ce-9b90-757bd26bbe24">
            <header>
  
  <div class="top-stripes"></div>
  
  <section class="ar-mobile-header">
    <div class="inner">
       <div class="logo-container" role="banner">
          <a href="/" class="logo"><img src="/pb-assets/assets/images/ar-logo-1479872034357.svg" width="50" height="50" alt="Annual Reviews home"></a>
       </div>
       <div class="mobile-links">
          <a href="#" class="icon-search-trigger icon-search" aria-label="site search"></a>
          <div data-widget-def="eCommerceCartIndicatorWidget" data-widget-id="66be61c1-70ea-4e40-8500-a50cf4d42ab7" class="mobile-cart">
             <a href="/action/showCart?FlowID=1" id="cartLabel">
                <div class="cartLabel">
                   <span class="icon-shoppingcart"></span>
                   <span class="filter-count filter-count-bubble shopping-cart hidden" data-id="cart-size">0</span>
                   <span class="cartText"></span>
                </div>
             </a>
          </div>
          <a href="#ar-mobile-nav" class="ar-mobile-nav" alt="Navigation menu"><span class="navicon"></span></a>
       </div>
    </div>
    <div class="mobile-search-container"></div>
 </section><!-- / .ar-mobile-header -->


  <section class="ar-desktop-header">
    <a href="#main-content" class="skip">Skip to content</a>
    <div class="newNavs">
      <!-- <div class="type-container"> -->
        <nav>
		<ul>
          <li><a href="/page/librarians/librarian-resource-page">For Librarians &amp; Agents</a></li>
          <li><a href="/page/authors/general-information">For Authors</a></li>
          <li><a href="https://www.knowablemagazine.org">Knowable Magazine</a></li>
        </ul>
		</nav>
        <div class="utility-nav-container">
            



    
    
        <div data-widget-def="literatumNavigationLoginBar" data-widget-id="db9e8c32-3723-4e61-ae84-3d4513efd55c">
            




    








    
        




    








    


















<div class="utility-nav">
    <nav>
        <ul>
            
                <li>
                    <a href="/action/ssostart">
                            Institutional Login
                    </a>
                </li>
            
            
                <li class="login">
                    <div class="loginBar">
                        <a href="/action/showLogin?redirectUri=%2Faction%2FshowPublications">
                            <span class="icon-profile_empty"></span>
                            <span class="sign-in-label">Login</span>
                        </a>
                    </div>
                </li>
            
            
                <li>
                    <a href="/action/registration?redirectUri=%2Faction%2FshowPublications">
                        Register
                    </a>
                </li>
            
            
                <li>
                    <a href="/page/activationForm.jsp">
                            Activate
                    </a>
                </li>
            

            
                <li>
                    <div class="pb-dropzone cartDropZone" data-pb-dropzone="cartDropZone">
                        
                            
                                



    
    
        <div data-widget-def="eCommerceCartIndicatorWidget" data-widget-id="788b9b05-39b3-4876-a174-a1f2c6e6a4d2">
            















<div class="eCommerceCartIndicatorWidget">
    
        
        
            <a href="/action/showCart?FlowID=1" id="cartLabel" title="Show shopping cart">
                <div class="cartLabel">
                    <span class="icon-shoppingcart"></span>
                    <span class="filter-count filter-count-bubble shopping-cart hidden"
                          data-id="cart-size">0</span>
                        
                    <span class="cartText">Cart</span>
                </div>
            </a>
        
    
</div>
        </div>
    



                            
                        
                    </div>
                </li>
            

            
                <li>
                    <a href="/help/main">
                            Help
                    </a>
                </li>
            
        </ul>
    </nav>
</div>

    
    


        </div>
    



        </div>
      <!-- </div>     -->
    </div>
    
    <div class="">
      <div class="utility-nav-container">
          <div class="access-provided">
            <div class="wrapper">
              <div class="inner">
                



    
    
        <div data-widget-def="literatumInstitutionBanner" data-widget-id="5a3d86ad-297b-48ae-a72b-2c175c813ea3">
            






















<div class="welcome">
    
    
    
        
            
            
                
            
        
    
</div>
        </div>
    



              </div>
            </div>
          </div>      
        </div>
      <div class="logo-container">
      <div class="logos">
        <a href="/"><div class="logo"><img src="/pb-assets/assets/images/ar-logo-1479872034357.svg" alt="Annual Reviews home"></div>
        <div class="ar-logo"><img src="/pb-assets/assets/images/logo-1453746913033.svg" alt=""></div></a>      
      </div>
      <div class="access-provided">
        <div class="wrapper">
          <div class="inner">
            



    
    
        <div data-widget-def="literatumInstitutionBanner" data-widget-id="d0fc4a47-d5bd-4e8e-86cf-f3bbe3f6abc3">
            






















<div class="welcome">
    
    
    
        
            
            
                
            
        
    
</div>
        </div>
    



          </div>
        </div>
      </div>
    </div>
    <div class="main-nav-container">
      <div class="main-nav-inner">
        <nav id="ar-main-nav" class="ar-main-nav" aria-label="site" role="navigation">
          <ul>
            <li class="has-dropdown full"><a aria-label="Annual Reviews journals A to Z" href="/action/showPublications">JOURNALS A-Z</a>
              <div class="ar-dropdown mega-dropdown">
                



    
    
        <div data-widget-def="literatumCategoryPublications" data-widget-id="a61e0a36-e95a-48ec-97ce-0b5c3703981d">
            <ul>
  
  
    
    
      
      <li class="publication" id="anchem">
        <a href="/journal/anchem">Analytical Chemistry</a>
      </li>
    
  
    
    
      
      <li class="publication" id="animal">
        <a href="/journal/animal">Animal Biosciences</a>
      </li>
    
  
    
    
      
      <li class="publication" id="anthro">
        <a href="/journal/anthro">Anthropology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="astro">
        <a href="/journal/astro">Astronomy and Astrophysics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="biochem">
        <a href="/journal/biochem">Biochemistry</a>
      </li>
    
  
    
    
      
      <li class="publication" id="biodatasci">
        <a href="/journal/biodatasci">Biomedical Data Science</a>
      </li>
    
  
    
    
      
      <li class="publication" id="bioeng">
        <a href="/journal/bioeng">Biomedical Engineering</a>
      </li>
    
  
    
    
      
      <li class="publication" id="biophys">
        <a href="/journal/biophys">Biophysics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="cancerbio">
        <a href="/journal/cancerbio">Cancer Biology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="cellbio">
        <a href="/journal/cellbio">Cell and Developmental Biology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="chembioeng">
        <a href="/journal/chembioeng">Chemical and Biomolecular Engineering</a>
      </li>
    
  
    
    
      
      <li class="publication" id="clinpsy">
        <a href="/journal/clinpsy">Clinical Psychology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="arcompsci">
        <a href="/journal/arcompsci">Computer Science</a>
      </li>
    
  
    
    
      
      <li class="publication" id="conmatphys">
        <a href="/journal/conmatphys">Condensed Matter Physics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="control">
        <a href="/journal/control">Control, Robotics, and Autonomous Systems</a>
      </li>
    
  
    
    
      
      <li class="publication" id="criminol">
        <a href="/journal/criminol">Criminology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="devpsych">
        <a href="/journal/devpsych">Developmental Psychology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="earth">
        <a href="/journal/earth">Earth and Planetary Sciences</a>
      </li>
    
  
    
    
      
      <li class="publication" id="ecolsys">
        <a href="/journal/ecolsys">Ecology, Evolution, and Systematics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="economics">
        <a href="/journal/economics">Economics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="ento">
        <a href="/journal/ento">Entomology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="energy">
        <a href="/journal/energy">Environment and Resources</a>
      </li>
    
  
    
    
      
      <li class="publication" id="financial">
        <a href="/journal/financial">Financial Economics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="fluid">
        <a href="/journal/fluid">Fluid Mechanics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="food">
        <a href="/journal/food">Food Science and Technology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="genet">
        <a href="/journal/genet">Genetics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="genom">
        <a href="/journal/genom">Genomics and Human Genetics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="immunol">
        <a href="/journal/immunol">Immunology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="lawsocsci">
        <a href="/journal/lawsocsci">Law and Social Science</a>
      </li>
    
  
    
    
      
      <li class="publication" id="linguistics">
        <a href="/journal/linguistics">Linguistics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="marine">
        <a href="/journal/marine">Marine Science</a>
      </li>
    
  
    
    
      
      <li class="publication" id="matsci">
        <a href="/journal/matsci">Materials Research</a>
      </li>
    
  
    
    
      
      <li class="publication" id="med">
        <a href="/journal/med">Medicine</a>
      </li>
    
  
    
    
      
      <li class="publication" id="micro">
        <a href="/journal/micro">Microbiology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="neuro">
        <a href="/journal/neuro">Neuroscience</a>
      </li>
    
  
    
    
      
      <li class="publication" id="nucl">
        <a href="/journal/nucl">Nuclear and Particle Science</a>
      </li>
    
  
    
    
      
      <li class="publication" id="nutr">
        <a href="/journal/nutr">Nutrition</a>
      </li>
    
  
    
    
      
      <li class="publication" id="orgpsych">
        <a href="/journal/orgpsych">Organizational Psychology and Organizational Behavior</a>
      </li>
    
  
    
    
      
      <li class="publication" id="pathmechdis">
        <a href="/journal/pathmechdis">Pathology: Mechanisms of Disease</a>
      </li>
    
  
    
    
      
      <li class="publication" id="pharmtox">
        <a href="/journal/pharmtox">Pharmacology and Toxicology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="physchem">
        <a href="/journal/physchem">Physical Chemistry</a>
      </li>
    
  
    
    
      
      <li class="publication" id="physiol">
        <a href="/journal/physiol">Physiology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="phyto">
        <a href="/journal/phyto">Phytopathology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="arplant">
        <a href="/journal/arplant">Plant Biology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="polisci">
        <a href="/journal/polisci">Political Science</a>
      </li>
    
  
    
    
      
      <li class="publication" id="psych">
        <a href="/journal/psych">Psychology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="publhealth">
        <a href="/journal/publhealth">Public Health</a>
      </li>
    
  
    
    
      
      <li class="publication" id="resource">
        <a href="/journal/resource">Resource Economics</a>
      </li>
    
  
    
    
      
      <li class="publication" id="soc">
        <a href="/journal/soc">Sociology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="statistics">
        <a href="/journal/statistics">Statistics and Its Application</a>
      </li>
    
  
    
    
      
      <li class="publication" id="virology">
        <a href="/journal/virology">Virology</a>
      </li>
    
  
    
    
      
      <li class="publication" id="vision">
        <a href="/journal/vision">Vision Science</a>
      </li>
    
  
  <li style="margin-top: 10px; padding-top: 10px; border-top: solid 1px #e5eaea;" class="publication">
    <a style="font-weight:600;" href="/page/collectionarchive">Article Collections</a>
  </li>
    <li class="publication">
    <a style="font-weight:600;" href="/page/events">Events</a>
  </li>
  <li class="publication">
    <a style="font-weight:600;" href="/shot-of-science">Shot of Science</a>
  </li>
</ul>

        </div>
    



              </div>
            </li>
            <li class="has-dropdown"><a aria-label="Information about Annual Reviews journals" href="/journal-info">JOURNAL INFO</a>
              <div class="ar-dropdown">
                <ul role="list" aria-expanded="true" aria-hidden="false">
                  <li><a href="/page/about/copyright-and-permissions">Copyright &amp; Permissions</a></li>
                  <li><a href="/page/help/coursereader">Add To Your Course Reader</a></li>
                  <li><a href="/page/journal/pubdates">Expected Publication Dates</a></li>
                  <li><a href="/page/about/isi-rankings" aria-label="journal impact factor rankings">Impact Factor Rankings</a></li>
                  <li><a href="/page/about/metadata">Access Metadata</a></li>
                  <li><a href="/page/about/rssfeeds" aria-label="Journal RSS feeds">RSS Feeds</a></li>
                </ul>
              </div>
            </li>
            <li class="has-dropdown"><a aria-label="Journal pricing and subscriptions" href="/page/subscriptions/general-information">PRICING &amp; SUBSCRIPTIONS</a>
              <div class="ar-dropdown">
                <ul role="list" aria-expanded="true" aria-hidden="false">
                  <li><a href="/page/subscriptions/general-information">General Ordering Info</a></li>
                  <li><a href="/page/subscriptions/online-activation-instructions">Online Activation Instructions</a></li>
                  <li><a href="/action/ecommerce?subscriberType=individual">Personal Pricing</a></li>
                  <li><a href="/page/subscriptions/instchoice">Institutional Pricing</a></li>
                  <li><a href="/page/about/society-partnerships">Society Partnerships</a></li>
                </ul>
              </div>
            </li>
			<li><a aria-label="S2O" href="/page/subscriptions/subscribe-to-open">&nbsp;&nbsp;&nbsp;&nbsp;S2O&nbsp;&nbsp;&nbsp;&nbsp;</a>
            </li>
            <li><a aria-label="Give to Annual Reviews" href="/support-annual-reviews">&nbsp;&nbsp;&nbsp;&nbsp;GIVE&nbsp;&nbsp;&nbsp;&nbsp;</a>
            </li>
            <li class="has-dropdown"><a aria-label="About Annual Reviews" href="/about">ABOUT</a>
              <div class="ar-dropdown">
                <ul role="list" aria-expanded="true" aria-hidden="false">
                  <li><a href="/about/what-we-do" aria-label="What we do">What We Do</a></li>
                  <li><a href="/about/our-founder-and-early-history">Founder &amp; History</a></li>
				  <!--<li><a href="/page/subscriptions/subscribe-to-open">Subscribe to Open</a></li>-->
                  <li><a href="/about/our-team">Our Team</a></li>
                  <li><a href="/page/about/careers-at-annual-reviews" aria-label="Careers at Annual Reviews">Careers</a></li>
                  <li><a href="/about/press-center">Press Center</a></li>
				  <li><a href="/page/events">Events</a></li>
                  <li><a href="http://www.annualreviewsnews.org" target="_blank" aria-label="News from Annual Reviews">News</a></li>
                  <li><a href="/about/global-access">Global Access</a></li>
				  <li><a href="/page/about/dei-committee">DEI</a></li>
                  <li><a href="/db/directory">Directory</a></li>
                  <li><a href="/help/main">Help/FAQs</a></li>
                  <li><a href="/page/about/contact-us" aria-label="Contact Annual Reviews">Contact Us</a></li>
                  </ul>
              </div>
            </li>
          </ul>
        </nav>
        <div class="ar-search-container">
          <div class="ar-main-search-form">
            <div class="inner">
              



    
    
        <div data-widget-def="quickSearchWidget" data-widget-id="0a761b65-b84e-45a2-8bc6-b82e2a128485">
            























<div class="quickSearchFormContainer">
    

    

    


    <form action="/action/doSearch" name="quickSearch" class="quickSearchForm " title="Quick Search" method="get"><span class="simpleSearchBoxContainer">
                        <input name="AllField"
               class="searchText magicsuggest main-search-field autocomplete"
               value=""
               type="search" id="searchText"
               title="Type search term here"
               placeholder="Enter words / phrases / DOI / ISBN / authors / keywords / etc." autocomplete="off"
               data-history-items-conf="3"
               data-publication-titles-conf="4"
               data-group-titles-conf="3"
               data-publication-items-conf="3"
               data-topics-conf="3"
               data-contributors-conf="3"
               data-display-labels="true"
               data-auto-complete-target="auto-complete"
               data-fuzzy-suggester="false"
               data-auto-complete-max-words="7"
               data-auto-complete-max-chars="32"/>
                        <input name="ConceptID"
               value=""
               type="hidden"/>
                </span>
                





    
    

        <span class="citationSearchBoxContainer hidden">
        <input name="quickLinkJournal" autoPopulate="true" data-auto-complete-target="title-auto-complete" autoComplete="off" type="search" title="Journal"
               class="journalName mediumTextInput  autocomplete" placeholder="Journal"/>

    


<input type="hidden" name="quickLink" value="true" />
<input type="hidden" name="quickLinkIssue" value="1" />
<input class="year smallTextInput" title="Year" type="search" name="quickLinkYear" value="" autocomplete="false" placeholder="Year" />
<input class="volume smallTextInput" title="Volume" type="search" name="quickLinkVolume" value="" autocomplete="false" placeholder="Volume" />
<input class="page smallTextInput" title="Page" type="search" name="quickLinkPage" value="" autocomplete="false" placeholder="Page" />
</span>

            
        

        

        
            




<input class="mainSearchButton searchButtons pointer" title="search" type="submit" value="Search" /></form>
</div>




<div class="advancedSearchLinkDropZone" data-pb-dropzone="advancedSearchLinkDropZone">
    
</div>
        </div>
    



            </div>
          </div>
          <a href="#" class="desktop-search-trigger icon-search"></a>
        </div>
      </div>
    </div>
  </section><!-- / .ar-desktop-header -->

</header>
        </div>
    



                        
                            



    
        <div data-widget-def="responsive-layout" data-widget-id="a553c5aa-19dc-427f-a22a-8dde5bfbff4a"
             
             class="journal-code-">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 main-content-container">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="44dedfee-08b0-4da2-a73f-09b5ee99e46b">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 ar-toolbar">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="f5e658a7-4e5c-4724-80d9-11685b2d8302">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-2 ar-breadcrumbs">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="literatumBreadcrumbs" data-widget-id="7e3ab43d-8bbc-479d-86d5-c2b2b7240420">
            





















<!-- Service: showPublications -->


    

    
    
        
        







































<!-- Service: showPublications -->

























    
    


    
    
        
    



    
    

    
    
        
        
            
        
    
    









    





<nav aria-label="breadcrumbs">
    <ul class="breadcrumbs">
        
        
            <li class="">

                
                    
                    
                    <a href="/">
                    Home
                    </a>
                    
                        <span class="divider">&gt;</span>
                    
                    
                
            </li>
        
            <li class="">

                
                    
                        
                        Browse
                    
                
            </li>
        
    </ul>
</nav>










    

    

    
        
    

    

    

    




        </div>
    



                        
                    
                </div>
            </div>
        
            <div class="col-md-1-2 ar-tools">
                <div class="contents" data-pb-dropzone="contents1">
                    
                    
                        
                            



    
        <div data-widget-def="layout-one-column" data-widget-id="43f7cc03-6b31-4308-8909-efef2f8a2811"
             
             class="addthis-wrapper">
            <div class="pb-columns row-fluid">
    <div class="width_1_1">
        <div data-pb-dropzone="center">




    
        <div data-widget-def="general-html" data-widget-id="0b9cc49a-cde0-4c2f-bd64-ffd2a512667f"
             
             class="ar-social-icon">
            <ul class="social-media-links">
  <li><a href="#" class="icon-email" title="Email" data-service="email"><span>Email</span></a></li>
  <li class="label">Share</li>
  <li><a href="#" class="icon-facebook" data-service="facebook" title="Share on Facebook" aria-label="Share on Facebook"></a></li>
  <li><a href="#" class="icon-twitter" data-service="twitter" title="Share on Twitter" aria-label="Share on Twitter"></a></li>
  <li><a href="#" class="icon-linkedin" data-service="linkedin" title="Share on LinkedIn" aria-label="Share on LinkedIn"></a></li>
  <li><a href="#" class="icon-reddit" data-service="reddit" title="Share on Reddit" aria-label="Share on Reddit"></a></li>
</ul>

</div>
    
    


        </div>
    </div>
</div>
</div>
    
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                            



    
    
        <div data-widget-def="general-html" data-widget-id="6961f603-aa72-429f-84e1-1b1e87aa35e8">
            <section class="ar-banner basic browse-journals" style="background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(/pb-assets/assets/images/banners/banner-default-1503337545653.jpg);">
    <div class="ar-banner-title-container">
      <div class="title">
        <h1>Browse  Journals</h1>
      </div>
    </div>
</section><!-- / .banner -->


        </div>
    



                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="5e17175e-82ce-464e-a554-dfcfd29769ca">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 ar-columns-container">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="97d12739-48ba-4636-81a5-2673432f07e2">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 inner">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="02865abf-b1c6-4f77-a829-5c78a90fb784">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 ar-content-full-col full-bleed">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="129cdacd-db21-4911-8745-b9cc625d37e1">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 browse-filter-bar">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="848634a2-561a-4a56-982a-7ac295f109f6">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 by-category">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
        <div data-widget-def="general-html" data-widget-id="3aaf60e4-b872-4cfe-9f32-8b35e7f02663"
             
             class="browse-journals-filter-header">
            <span class="header icon-filter">FILTER BY CATEGORY:</span>

</div>
    
    



                        
                            



    
        <div data-widget-def="literatumPublicationBrowseSidebar" data-widget-id="f282197a-0616-40d2-aab6-82461b1d2ac0"
             
             class="browse-journals-filters">
            




<!-- this is all categories -->

    
    
        
            
            
                <a href="/action/showPublications">All Subjects</a>
            
        
    



<div class="subjectOutlineContainer">
    <ul class="subjectListing">
        
            
                












<li class="subjectList">
    <span  >
          <a href="/action/showPublications?category=10.5555%2Fcategory.576">Biomedical/Life Sciences <span class="pub-count">(32)</span></a>
    </span>
    
</li>
            
        
            
                












<li class="subjectList">
    <span  >
          <a href="/action/showPublications?category=10.5555%2Fcategory.577">Physical Sciences <span class="pub-count">(16)</span></a>
    </span>
    
</li>
            
        
            
                












<li class="subjectList">
    <span  >
          <a href="/action/showPublications?category=10.5555%2Fcategory.578">Social Sciences <span class="pub-count">(16)</span></a>
    </span>
    
        <ul class="subjectListing">
            
                
                    












<li class="subjectList">
    <span  >
          <a href="/action/showPublications?category=10.1555%2Fcategory.40002344">Economics <span class="pub-count">(3)</span></a>
    </span>
    
</li>
                
            
        </ul>
    
</li>
            
        
    </ul>
</div></div>
    
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                            



    
    
        <div data-widget-def="responsive-layout" data-widget-id="b5cbe92e-661b-4c80-a65f-d61877901139">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 browse-journals-container">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="general-html-asset" data-widget-id="e411ebaa-32ad-4c2d-bdcb-34c4432ccdb6">
            



    
    
        <div data-widget-def="literatumCategoryPublications" data-widget-id="de749ba8-3cb4-492e-9a52-f7d7c2f658f1">
            
  
    <div class="ar-browse-item">
      <!-- <a href="/journal/anchem" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/anchem" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-anchem-1473890225587.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Analytical Chemistry</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Analytical Chemistry</div>
              <p>
                Aimed at readers interested in physical, chemical, and biological measurements. Draws from disciplines as diverse as biology, physics, and engineering.
              </p>
              <!--<p>
                Latest Volume: 15
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/animal" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/animal" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-animal-1473890225580.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Animal Biosciences</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Animal Biosciences</div>
              <p>
                Topics include biotechnology, genetics, genomics, and breeding; veterinary medicine, and conservation and zoo biology. Intended for veterinarians, geneticists, and scientists focused on domesticated and wild animal species.
              </p>
              <!--<p>
                Latest Volume: 10
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/anthro" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/anthro" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-anthro-1473890235497.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Anthropology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Anthropology</div>
              <p>
                Topics include archaeology, biological anthropology, linguistics and communicative practices, regional studies and international anthropology, and sociocultural anthropology.
              </p>
              <!--<p>
                Latest Volume: 51
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/astro" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/astro" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-astro-1473890234917.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Astronomy and Astrophysics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Astronomy and Astrophysics</div>
              <p>
                Topics include the sun, solar system and extrasolar planets, stars, galaxies, active galactic nuclei, cosmology, and instrumentation and techniques.
              </p>
              <!--<p>
                Latest Volume: 60
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/biochem" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/biochem" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-biochem-1473890234437.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Biochemistry</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Biochemistry</div>
              <p>
                The flagship Annual Reviews journal, it sets the standard for review articles in biological chemistry and molecular biology and serves as an indispensable resource for practicing biochemists and their students. Publishing since 1932.
              </p>
              <!--<p>
                Latest Volume: 91
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/biodatasci" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/biodatasci" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-biodatasci-1522345191517.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Biomedical Data Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Biomedical Data Science</div>
              <p>
                Provides comprehensive reviews in biomedical data science, focusing on advanced methods to store, retrieve, analyze, and organize biomedical data and knowledge.
              </p>
              <!--<p>
                Latest Volume: 5
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/bioeng" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/bioeng" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-bioeng-1473890234210.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Biomedical Engineering</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Biomedical Engineering</div>
              <p>
                Topics include biomechanics, biomaterials, computational genomics and proteomics, tissue engineering, health care engineering, drug delivery, bioelectrical engineering, biochemical engineering, and biomedical imaging.
              </p>
              <!--<p>
                Latest Volume: 24
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/biophys" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/biophys" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-biophys-1473890233957.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Biophysics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Biophysics</div>
              <p>
                Topics include macromolecular structure, function and dynamics, theoretical and computational biophysics, molecular biophysics of the cell, physical systems biology, membrane biophysics, nanotechnology, and emerging techniques.
              </p>
              <!--<p>
                Latest Volume: 51
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/cancerbio" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/cancerbio" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-cancerbio-1479754752933.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Cancer Biology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Cancer Biology</div>
              <p>
                Reviews a range of subjects in cancer research that represent important and emerging developments, and is divided into three broad themes: Cancer Cell Biology, Tumorigenesis and Cancer Progression, and Translational Cancer Science.
              </p>
              <!--<p>
                Latest Volume: 6
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/cellbio" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/cellbio" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-cellbio-1473890233517.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Cell and Developmental Biology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Cell and Developmental Biology</div>
              <p>
                Topics include the structure, function, and organization of the cell; development and evolution of the cell in single and multicellular organisms; and models and tools of molecular biology.
              </p>
              <!--<p>
                Latest Volume: 38
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/chembioeng" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/chembioeng" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-chembioeng-1473890232873.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Chemical and Biomolecular Engineering</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Chemical and Biomolecular Engineering</div>
              <p>
                Aimed at readers with a general background in the natural sciences, including scientists and engineers interested in physical, chemical, and biological phenomena toward advances in chemical process design and new products.
              </p>
              <!--<p>
                Latest Volume: 13
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/clinpsy" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/clinpsy" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-clinpsy-1479754753630.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Clinical Psychology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Clinical Psychology</div>
              <p>
                Topics explore the research, theory, and the application of psychological principles to address recognized disorders, including schizophrenia as well as mood, anxiety, childhood, substance use, cognitive, and personality disorders.
              </p>
              <!--<p>
                Latest Volume: 18
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/arcompsci" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/arcompsci" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-arcompsci-1473890235380.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Computer Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Computer Science</div>
              <p>
                This series has been discontinued. Volumes available: 1-4, 1986-1990
              </p>
              <!--<p>
                Latest Volume: 4
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/conmatphys" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/conmatphys" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-conmatphys-1473890232687.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Condensed Matter Physics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Condensed Matter Physics</div>
              <p>
                Topics explore related research areas in materials science and biology.
              </p>
              <!--<p>
                Latest Volume: 13
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/control" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/control" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-control-1522345201443.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Control, Robotics, and Autonomous Systems</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Control, Robotics, and Autonomous Systems</div>
              <p>
                The broad fields of control and robotics are the major areas covered, together with connections to theoretical and applied mechanics, optimization, communication, information theory, machine learning, computing, and signal processing.
              </p>
              <!--<p>
                Latest Volume: 5
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/criminol" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/criminol" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-criminol-1503688727203.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Criminology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Criminology</div>
              <p>
                Provides comprehensive reviews of significant developments in the multidisciplinary field of criminology, defined as the study of both the nature of criminal behavior and societal reactions to crime.
              </p>
              <!--<p>
                Latest Volume: 5
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/devpsych" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/devpsych" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-devpsych-1576183786707.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Developmental Psychology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Developmental Psychology</div>
              <p>
                Covers the significant advances in the developmental sciences, including cognitive, linguistic, social, cultural, and biological processes across the lifespan.
              </p>
              <!--<p>
                Latest Volume: 3
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/earth" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/earth" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-earth-1473890232577.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Earth and Planetary Sciences</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Earth and Planetary Sciences</div>
              <p>
                Topics range from the climate, environment, and geological hazards to the formation of planets and the evolution of life.
              </p>
              <!--<p>
                Latest Volume: 50
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/ecolsys" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/ecolsys" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-ecolsys-1473890232357.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Ecology, Evolution, and Systematics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Ecology, Evolution, and Systematics</div>
              <p>
                Articles range from phylogeny, speciation, and molecular evolution through behavior and evolutionary physiology to population dynamics, ecosystems processes, and applications in invasion biology, conservation, and management.
              </p>
              <!--<p>
                Latest Volume: 53
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/economics" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/economics" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-economics-1479496313430.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Economics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Economics</div>
              <p>
                Topics include macroeconomics and money; microeconomics, including economic psychology; international economics; public finance; health economics; economic growth and technological change; development; and social economics.
              </p>
              <!--<p>
                Latest Volume: 14
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/ento" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/ento" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-ento-1473890231703.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Entomology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Entomology</div>
              <p>
                Topics include biochemistry and physiology, morphology and development, behavior and neuroscience, ecology, agricultural entomology, pest management, biological control, medical and veterinary entomology, and biogeography.
              </p>
              <!--<p>
                Latest Volume: 67
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/energy" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/energy" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-energy-1473890232007.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Environment and Resources</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Environment and Resources</div>
              <p>
                Covers the advances and emerging issues in environmental science. Topics include ecology and conservation science, agriculture and living resources, engineering, water and energy resources, atmosphere, oceans, climate change.
              </p>
              <!--<p>
                Latest Volume: 47
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/financial" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/financial" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-financial-1473890231487.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Financial Economics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Financial Economics</div>
              <p>
                Topics include theoretical, empirical, and experimental developments in financial economics; capital markets, corporate finance, financial institutions, market microstructure, and behavioral and experimental finance.
              </p>
              <!--<p>
                Latest Volume: 14
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/fluid" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/fluid" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-fluid-1473890231187.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Fluid Mechanics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Fluid Mechanics</div>
              <p>
                Topics include non-Newtonian fluids and rheology, incompressible and compressible fluids, plasma flow, stability of flow, multi-phase flows, mixing and transport of heat and species, combustion, turbulence, shock waves and explosions.
              </p>
              <!--<p>
                Latest Volume: 54
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/food" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/food" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-food-1479754753863.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Food Science and Technology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Food Science and Technology</div>
              <p>
                Topics include food microbiology, food-borne pathogens, fermentation, food engineering, biochemistry, rheology, and sensory properties; novel ingredients and nutrigenomics; emerging technologies in food processing and preservation.
              </p>
              <!--<p>
                Latest Volume: 13
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/genet" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/genet" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-genet-1473890230863.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Genetics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Genetics</div>
              <p>
                Topics include biochemical, behavioral, cell, and developmental genetics; evolutionary and population genetics; chromosome structure and transmission; gene function and expression; mutation and repair; genomics; immunogenetics.
              </p>
              <!--<p>
                Latest Volume: 56
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/genom" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/genom" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-genom-1473890230717.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Genomics and Human Genetics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Genomics and Human Genetics</div>
              <p>
                Explores genomics as it applies to human genetics and the human genome. Topics include genomic technology, genome structure and function, genetic modification, human variation and population genetics, and human evolution.
              </p>
              <!--<p>
                Latest Volume: 23
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/immunol" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/immunol" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-immunol-1473890230603.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Immunology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Immunology</div>
              <p>
                Focuses on immune mechanisms and molecular basis of immune diseases in humans. Topics include immune cell development and differentiation; immune control of pathogens and cancer; and immunodeficiency and autoimmune diseases.
              </p>
              <!--<p>
                Latest Volume: 40
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/lawsocsci" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/lawsocsci" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-lawsocsci-1473890230343.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Law and Social Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Law and Social Science</div>
              <p>
                Draws on the complex connections between law, culture, social structure, and society by focusing on social scientific studies of law and law-like systems of rules, institutions, processes, and behaviors.
              </p>
              <!--<p>
                Latest Volume: 18
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/linguistics" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/linguistics" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-linguistics-1592868398640.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Linguistics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Linguistics</div>
              <p>
                Covers significant developments in linguistics, including phonetics, phonology, morphology, syntax, semantics, pragmatics, and their interfaces, linguistic theory, sociolinguistics, psycholinguistics, neurolinguistics, language change, as well as applications of linguistics in many domains.
              </p>
              <!--<p>
                Latest Volume: 8
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/marine" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/marine" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-marine-1473890229910.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Marine Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Marine Science</div>
              <p>
                Draws from topics within coastal and blue water oceanography (biological, chemical, geological, physical) as well as subjects in ecology, conservation, technological developments within the marine environment.
              </p>
              <!--<p>
                Latest Volume: 14
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/matsci" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/matsci" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-matsci-1473890229797.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Materials Research</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Materials Research</div>
              <p>
                Topics include original methodologies, materials phenomena, and material systems.
              </p>
              <!--<p>
                Latest Volume: 52
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/med" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/med" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-med-1473890229480.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Medicine</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Medicine</div>
              <p>
                Topics include immunology, cardiology, dermatology, endocrinology, gastroenterology, genetics, infectious disease, neurology, oncology/hematology, pediatrics, psychiatry, pulmonology, reproductive medicine, surgery.
              </p>
              <!--<p>
                Latest Volume: 73
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/micro" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/micro" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-micro-1473890229410.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Microbiology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Microbiology</div>
              <p>
                Topics include bacteria, archaea, viruses, and unicellular eukaryotes. Draws from a broad group of disciplines, ranging from ecology and evolution to biochemistry, genomics, and structural biology.
              </p>
              <!--<p>
                Latest Volume: 76
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/neuro" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/neuro" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-neuro-1473890229007.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Neuroscience</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Neuroscience</div>
              <p>
                Topics include molecular and cellular neuroscience, neurogenetics, development, plasticity and repair, systems neuroscience, cognitive neuroscience, behavior, neurobiology of disease, and ethics.
              </p>
              <!--<p>
                Latest Volume: 45
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/nucl" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/nucl" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-nucl-1473890228683.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Nuclear and Particle Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Nuclear and Particle Science</div>
              <p>
                Topics include theoretical developments, experimental results and their interpretation, heavy ion interactions, oscillations observed in solar and atmospheric neutrinos, the physics of heavy quarks, the impact of particle and nuclear physics on astroparticle physics.
              </p>
              <!--<p>
                Latest Volume: 72
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/nutr" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/nutr" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-nutr-1483974718587.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Nutrition</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Nutrition</div>
              <p>
                Topics include metabolism, carbohydrates, lipids, proteins and amino acids, nutrient transport and function, metabolic regulation, nutritional genomics, clinical nutrition, nutritional toxicology and microbiology, epidemiology, and public health.
              </p>
              <!--<p>
                Latest Volume: 42
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/orgpsych" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/orgpsych" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-orgpsych-1479754753950.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Organizational Psychology and Organizational Behavior</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Organizational Psychology and Organizational Behavior</div>
              <p>
                Topics include industrial and organizational psychology, human resource management, and organizational behavior.
              </p>
              <!--<p>
                Latest Volume: 9
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/pathmechdis" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/pathmechdis" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-pathmechdis-1479754754093.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Pathology: Mechanisms of Disease</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Pathology: Mechanisms of Disease</div>
              <p>
                Focuses on understanding the initiation and progression of human diseases. Topics include evolving concepts of disease pathogenesis, molecular, genetic and morphologic alterations associated with diseases, and clinical significance.
              </p>
              <!--<p>
                Latest Volume: 17
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/pharmtox" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/pharmtox" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-pharmtox-1473890228393.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Pharmacology and Toxicology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Pharmacology and Toxicology</div>
              <p>
                Topics include receptors, transporters, enzymes, and chemical agents; drug development science; and the immune system, central and autonomic nervous systems, gastrointestinal, cardiovascular, endocrine, and pulmonary systems.
              </p>
              <!--<p>
                Latest Volume: 62
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/physchem" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/physchem" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-physchem-1473890228117.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Physical Chemistry</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Physical Chemistry</div>
              <p>
                Topics include biophysical chemistry, chemical kinetics, colloids, electrochemistry, geochemistry, cosmochemistry, chemistry of atmosphere and climate, laser chemistry, the liquid state, polymers, and macromolecules.
              </p>
              <!--<p>
                Latest Volume: 73
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/physiol" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/physiol" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-physiol-1473890227790.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Physiology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Physiology</div>
              <p>
                Topics include cardiovascular physiology; cell physiology; ecological, evolutionary, and comparative physiology; endocrinology; gastrointestinal physiology; neurophysiology; renal/electrolyte physiology; respiratory physiology.
              </p>
              <!--<p>
                Latest Volume: 84
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/phyto" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/phyto" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-phyto-1483974737697.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Phytopathology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Phytopathology</div>
              <p>
                Topics include plant disease diagnosis, pathogens, host-pathogen interactions, epidemiology and ecology, breeding for resistance, and plant disease management. Includes special section on the development of concepts.
              </p>
              <!--<p>
                Latest Volume: 60
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/arplant" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/arplant" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-arplant-1473890235070.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Plant Biology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Plant Biology</div>
              <p>
                Topics include plant biochemistry and biosynthesis; genetics, genomics; and molecular biology; cell differentiation; tissue; organ and whole-plant events; acclimation and adaptation, and methods and model organisms.
              </p>
              <!--<p>
                Latest Volume: 73
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/polisci" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/polisci" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-polisci-1473890226973.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Political Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Political Science</div>
              <p>
                Topics include political theory and philosophy, international relations, political economy, political behavior, American and comparative politics, public administration and policy, and methodology.
              </p>
              <!--<p>
                Latest Volume: 25
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/psych" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/psych" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-psych-1473890226857.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Psychology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Psychology</div>
              <p>
                Topics include the biological bases of behavior, sensation and perception, cognitive processes, animal learning/behavior, human development, psychopathology, clinical and counseling psychology, and social/environmental/community psychology.
              </p>
              <!--<p>
                Latest Volume: 73
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/publhealth" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/publhealth" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-publhealth-1483974729560.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Public Health</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Public Health</div>
              <p>
                Topics include key developments in epidemiology and biostatistics, environmental and occupational health, issues related to social environment and behavior, health services, and public health practice.
              </p>
              <!--<p>
                Latest Volume: 43
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/resource" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/resource" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-resource-1473890226503.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Resource Economics</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Resource Economics</div>
              <p>
                Focuses on agricultural economics, environmental economics, renewable resources, and exhaustible resources.
              </p>
              <!--<p>
                Latest Volume: 14
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/soc" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/soc" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-soc-1473890226370.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Sociology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Sociology</div>
              <p>
                Articles cover social processes, institutions and culture, organizations, political and economic sociology, stratification, demography, urban sociology, social policy, and historical sociology.
              </p>
              <!--<p>
                Latest Volume: 48
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/statistics" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/statistics" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-statistics-1473890226267.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Statistics and Its Application</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Statistics and Its Application</div>
              <p>
                Topics include theoretical statistical underpinnings of new methodology and specific domains such as biostatistics and bioinformatics, economics, machine learning, psychology, sociology, and aspects of the physical sciences.
              </p>
              <!--<p>
                Latest Volume: 9
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/virology" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/virology" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-virology-1473890226027.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Virology</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Virology</div>
              <p>
                Topics include viruses of animals, plants, bacteria, archaea, fungi, and protozoa. Reviews will inform basic virology, viral disease mechanisms, virus-host interactions, and cellular and immune responses to virus infection.
              </p>
              <!--<p>
                Latest Volume: 9
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  

  
    <div class="ar-browse-item">
      <!-- <a href="/journal/vision" style="background-image: url(http://www.unsplash.it/640?image=10);"> -->
      <a href="/journal/vision" style="background-image: url(/pb-assets/assets/images/journal-covers/journal-cover-vision-1473890225580.jpg);">
        <div class="text-container front">
          <div>
            <span>
              <div class="title">Vision Science</div>
            </span>
          </div>
        </div>
        <div class="text-container back">
          <div>
            <span>
              <div class="title">Vision Science</div>
              <p>
                Covers progress in the visual sciences, a cross-cutting set of disciplines which intersect psychology, neuroscience, computer science, cell biology and genetics, and clinical medicine. The study of vision is central to progress in many areas of science.
              </p>
              <!--<p>
                Latest Volume: 8
              </p>-->
            </span>
          </div>
        </div>
      </a>
    </div>
  


        </div>
    




        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div></div>
    
    



                        
                            



    
    
        <div data-widget-def="pageFooter" data-widget-id="82661446-9211-42a4-ba53-6c041475df5d">
            <footer class="page-footer">
    <div data-pb-dropzone="main">
    



    
    
        <div data-widget-def="responsive-layout" data-widget-id="d70bad86-313a-4f32-ae0b-23f8e62e5859">
            




    
    
        
    

<div class="container-fluid">
    <div class="row row-md  ">
        
            <div class="col-md-1-1 inner-content">
                <div class="contents" data-pb-dropzone="contents0">
                    
                    
                        
                            



    
    
        <div data-widget-def="general-html" data-widget-id="2d5aba52-2a85-4951-a711-4a3850c71db7">
            <section class="footer-links">
    <ul>
        <li>&copy; <a href="/page/about/trademark">Copyright 2022</a></li>
        <li><a href="/page/about/contact-us">Contact Us</a></li>
        <li><a href="/userpreferencecenter">Email Preferences</a></li>
        <li><a href="/db/directory">Annual Reviews Directory</a></li>
        <li><a href="/topic/multimedia?target=do-topic">Multimedia</a></li>
        <li><a href="/db/suppl">Supplemental Materials</a></li>
        <li><a href="/page/about/faq" aria-label="Frequently asked questions">FAQs</a></li>
        <li><a href="/page/about/privacy">Privacy Policy</a></li>
        <li><a class="ot-sdk-show-settings">Cookie Preferences</a></li>
    </ul>
</section>
<section class="social-links">
    <ul>
        <li><a href="https://www.facebook.com/AnnualReviews" class="icon-facebook" target="_blank" aria-label="Share on Facebook"></a></li>
        <li><a href="https://twitter.com/AnnualReviews" class="icon-twitter" target="_blank" aria-label="Share on Twitter"></a></li>
        <li><a href="https://www.linkedin.com/company/annual-reviews" class="icon-linkedin" target="_blank" aria-label="Share on LinkedIn"></a></li>
        <li><a href="/page/about/rssfeeds" class="icon-rss" target="_blank" aria-label="Follow us via RSS"></a></li>
        <li><a href="https://www.youtube.com/user/annualreviews" class="icon-youtube" aria-label="Annual Reviews YouTube Channel" target="_blank"></a></li>
    </ul>
</section>


        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    


    </div>
</footer>
        </div>
    



                        
                    
                </div>
            </div>
        
    </div>
</div>
        </div>
    






    
    
        <div data-widget-def="general-html" data-widget-id="4732cf84-b8b3-4bbf-abf4-25b396cffdc2">
            <nav id="ar-mobile-nav"></nav>


        </div>
    






    
    
        <div data-widget-def="general-html" data-widget-id="3f1ce15a-0230-4676-a7ec-ab40e3028631">
            <!-- Plugins -->
      
<!--[if lt IE 10]>
    <script src="/pb-assets/assets/js/plugins/matchMedia-1453746996263.js"></script>
    <script src="/pb-assets/assets/js/plugins/matchMedia.addListener-1453746994877.js"></script>
    <script src="/pb-assets/assets/js/plugins/placeholders.min-1453746997600.js"></script>
<![endif]-->

<script src="/pb-assets/bower_components/enquire/dist/enquire.min-1447876631343.js"></script>
<script src="/pb-assets/bower_components/jQuery.mmenu/dist/core/js/jquery.mmenu.min-1447876913397.js"></script>
<script src="/pb-assets/bower_components/matchHeight/jquery.matchHeight-min-1447877055877.js"></script>
<script src="/pb-assets/assets/js/plugins/listsplitter-1453746992453.js"></script>
<script src="/pb-assets/bower_components/magnific-popup/dist/jquery.magnific-popup.min-1469098659783.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tooltipster/3.3.0/js/jquery.tooltipster.js"></script>

<!-- Main js -->
<script src="/pb-assets/assets/js/all.min-1665924253073.js"></script>


        </div>
    






    
    
        <div data-widget-def="general-html" data-widget-id="d21f7f44-3935-4c7d-bf0c-65f76475a418">
            <!-- Bot analytics test -->
<script src="https://api.b2c.com/api/init-260u9k3l7hxtcferh76.js" data-cfasync="false" async></script>
<noscript><img src="https://api.b2c.com/api/noscript-260u9k3l7hxtcferh76.gif"></noscript>



        </div>
    






    
    
        <div data-widget-def="general-html" data-widget-id="31fef650-8d92-48d8-b29e-038e4fd7ac17">
            <script>
$(document).ready(function() {
          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
        
          ga('create', 'UA-1828393-3', 'auto');
          ga('set', 'anonymizeIp', true);

            
            $('.ar-main-search-form .inner input.mainSearchButton').on('click', function() {
                if ($('div.ar-main-search-form').hasClass('active') && $('form input#searchText').val().length != 0) {
                    txt = $('form input#searchText').val();
                    //alert("hey " +txt);
                    ga('send','event','ar_SearchBox','click', txt);
                }
                else if ($('div.mobile-search-container').hasClass('active') && $('form input.searchText').val().length != 0) {
                    txt = $('form input.searchText').val();
                    //alert("hey " +txt);
                    ga('send','event','ar_SearchBox','click', txt);
                }
            });
            
             //added on 22AUG17
            //PUBLISHED IN field on Advanced Search form
            $('#submitPubSearchButton').on('click', function(){
            var term = "";
                if ($('div.ms-sel-item').text() != "") {
                    $('div.ms-sel-ctn > div.ms-sel-item').each(function(){
                        term += $(this).text() + " | ";
                    })
                    //alert(txt);
                    ga('send','event','search_PublishedIntxt','click', term);
                };
            });
            
            //added on 24AUG17
            //Advanced Search tabs
            var $search_JournalContentTab = $('#searchResultContainer li a:contains("Journal Content")');
            var $search_FiguresTablesTab = $('#searchResultContainer li a:contains("Figures/Tables")');
            var $search_SupplementalMaterialsTab = $('#searchResultContainer li a:contains("Supplemental Material")');
            var $search_GeneralInfoTab = $('#searchResultContainer li a:contains("General Info")');
            var $search_MultimediaTab = $('#searchResultContainer li a:contains("Multimedia")');

            //Sending Events for Advanced Search tabs hits
            $search_JournalContentTab.on('click', function() {
                url = window.location.href;
                ga('send','event','search_JournalContentTab','click', url);
            });
            $search_FiguresTablesTab.on('click', function() {
                url = window.location.href;
                ga('send','event','search_FiguresTablesTab','click', url);
            });
            $search_SupplementalMaterialsTab.on('click', function() {
                url = window.location.href;
                ga('send','event','search_SupplementalMaterialsTab','click', url);
            });
            $search_GeneralInfoTab.on('click', function() {
                url = window.location.href;
                ga('send','event','search_GeneralInfoTab','click', url);
            });
            $search_MultimediaTab.on('click', function() {
                url = window.location.href;
                ga('send','event','search_MultimediaTab','click', url);
            });
            
            // AR Homepage
            // added 31AUG17
            var $homepageSlider_PrevBtn = $('div.home-slider button.flickity-prev-next-button.previous');
            var $homepageSlider_NextBtn = $('div.home-slider button.flickity-prev-next-button.next');
            
            // Sending Events for AR Homepage Slider
            $homepageSlider_PrevBtn.click(function(){
                url = window.location.href;
                ga('send','event','homepageSlider_PrevBtn','click', url);
            });
            $homepageSlider_NextBtn.click(function(){
                url = window.location.href;
                ga('send','event','homepageSlider_NextBtn','click', url);
            });
            
            // Search Results preview tab
            // added on 31AUG17
            var $searchResults_Previewtab = $('div.listings ol.search-results .journal-preview-container');
            // Sending Events for Search Results preview tab
            $searchResults_Previewtab.click(function(){
                if($(this).find('span.preview-trigger').text() === "Hide"){
        			title = $(this).parent().attr('data-title');
                    url = window.location.href;
                    entireTerm = title + " | " + url;
                    ga('send','event','searchResults_Previewtab','click', entireTerm);
                }
            });
            
            //TOC Checkbox widget
            //added on 18APR18
            $( "select.publicationToolSelect" ).change( displayVals );
            
            function displayVals() {
              var singleValues = $( ".publicationToolSelect :selected" ).text();
              var multipleValues = $( ".teaser input:checkbox:checked").map(function(){
                  return $(this).parent().text();
                }).get();
              var mValues = multipleValues.join( " | " );
              
              var finalValues = "Dropdown Value: " + singleValues + " ..AND.. Items checked: " + mValues;
              ga('send','event','TOC_CheckboxWidget','click', finalValues);
            }
            
            //Preview Abstract tab on Current TOC pages
            //added on 23APR18
            var $TOC_previewABSTab = $('.tocListWidgetContainer .teaser .journal-preview-bar');

            // Sending Events for Search Results preview tab
            $TOC_previewABSTab.click(function(){
                if($(this).find('span.preview-trigger').text() === "Hide"){
        			titleArticle = $(this).parent(".journal-preview-container").siblings(".row").find(".text h2").text();
                    url = window.location.href;
                    Term = titleArticle + " | " + url;
                    ga('send','event','TOC_previewABSTab','click', Term);
                }
            });
            
            // TOC Selector on Volume Pages
            $('#toc-selector select.volume').change(function(){ 
                url = window.location.href;
                var Volume_TOC_Selector = $("#toc-selector select.volume option:selected").val();
              	ga('send','event','Volume_TOC_Selector','click', Volume_TOC_Selector);
            })
});
</script>


        </div>
    






    
    
        <div data-widget-def="general-html-asset" data-widget-id="5c4d8202-49f2-48de-bf1c-0a05dc242323">
            <script>
  var appsMenuItems = document.querySelectorAll('#ar-main-nav > ul > li');
  var subMenuItems = document.querySelectorAll('#ar-main-nav > ul > li li');
  var keys = {
    tab:    9,
    enter:  13,
    esc:    27,
    space:  32,
    left:   37,
    up:     38,
    right:  39,
    down:   40
  };
  var currentIndex, subIndex;
  
  var gotoIndex = function(idx) {
    if (idx == appsMenuItems.length) {
      // idx = 0;
    } else if (idx < 0) {
      idx = appsMenuItems.length - 1;
    }
    appsMenuItems[idx].focus();
    appsMenuItems[idx].querySelector('a').focus();
    currentIndex = idx;
  };
  
  var gotoIndexItem = function(idx) {
    if (idx == appsMenuItems.length) {
      // idx = 0;
    } else if (idx < 0) {
      idx = appsMenuItems.length - 1;
    }
    // appsMenuItems[idx].focus();
    appsMenuItems[idx].querySelector('a').focus();
    currentIndex = idx;
  };
  
  var gotoSubIndex = function (menu, idx) {
    var items = menu.querySelectorAll('li');
    if (idx == items.length) {
      idx = 0;
    } else if (idx < 0) {
      idx = items.length - 1;
    }
    items[idx].focus();
    subIndex = idx;
  };
  
  var gotoSubIndexItem = function (menu, idx) {
    var items = menu.querySelectorAll('li > a');
    if (idx == items.length) {
      // idx = 0;
    } else if (idx < 0) {
      idx = items.length - 1;
    }
    items[idx].click();
    subIndex = idx;
  };
  
  Array.prototype.forEach.call(appsMenuItems, function(el, i){
    if (0 == i) {
      el.setAttribute('tabindex', '0');
      el.addEventListener("focus", function() {
          currentIndex = 0;
      });
    } else {
      el.setAttribute('tabindex', '-1');
    }
    el.addEventListener("focus", function() {
      subIndex = 0;
      Array.prototype.forEach.call(appsMenuItems, function(el, i){
          el.setAttribute('aria-expanded', "false");
      });
    });
    el.addEventListener("click",  function(event){
      if (this.getAttribute('aria-expanded') == 'false' || this.getAttribute('aria-expanded') ==  null) {
          this.setAttribute('aria-expanded', "true");
      } else {
          this.setAttribute('aria-expanded', "false");
      }
      // event.preventDefault();
      return true;
    });
    el.addEventListener("keydown", function(event) {
      var prevdef = false;
      switch (event.keyCode) {
          case keys.right:
            gotoIndex(currentIndex + 1);
            prevdef = true;
            break;
          case keys.left:
            gotoIndex(currentIndex - 1);
            prevdef = true;
            break;
          case keys.tab:
            if (event.shiftKey) {
                  gotoIndex(currentIndex - 1);
            } else {
                  gotoIndex(currentIndex + 1);
            }
            prevdef = true;
            break;
          case keys.enter:
          // $(this).find('a').focus();
          // gotoIndexItem(currentIndex);
          // gotoSubIndexItem(this.parentNode, subIndex)
          // alert(this.innerText);
          gotoIndexItem(currentIndex);
          return true;
          break;
          case keys.down:
            if(this.innerText === 'JOURNALS A-Z') {
                break;
            }
            this.click();
            subindex = 0;
            gotoSubIndex(this.querySelector('ul'), 0);
            prevdef = true;
            break;
          case keys.up:
            if(this.innerText === 'JOURNALS A-Z') {
                break;
            }
            this.click();
            var submenu = this.querySelector('ul');
            subindex = submenu.querySelectorAll('li').length - 1;
            gotoSubIndex(submenu, subindex);
            prevdef = true;
            break;
          case keys.esc:
            document.querySelector('#escape').setAttribute('tabindex', '-1');
            document.querySelector('#escape').focus();
            prevdef = true;
          }
          if (prevdef) {
            event.preventDefault();
          }
    });
  });
  
  Array.prototype.forEach.call(subMenuItems, function(el, i){
    el.setAttribute('tabindex', '-1');
    el.addEventListener("keydown", function(event) {
      switch (event.keyCode) {
        case keys.tab:
          if (event.shiftKey) {
                gotoIndex(currentIndex - 1);
          } else {
                gotoIndex(currentIndex + 1);
          }
          prevdef = true;
          break;
        case keys.right:
          gotoIndex(currentIndex + 1);
          prevdef = true;
          break;
        case keys.left:
          gotoIndex(currentIndex - 1);
          prevdef = true;
          break;
        case keys.esc:
          gotoIndex(currentIndex);
          prevdef = true;
          break;
        case keys.down:
          gotoSubIndex(this.parentNode, subIndex + 1);
          prevdef = true;
          break;
        case keys.up:
          gotoSubIndex(this.parentNode, subIndex - 1);
          prevdef = true;
          break;
        case keys.enter:
        // $(this).find('a').focus();
        gotoSubIndexItem(this.parentNode, subIndex);					
        return true;
        break;
        case keys.space:
          // alert(this.innerText);
          prevdef = true;
          break;
      }
      if (prevdef) {
        event.preventDefault();
        event.stopPropagation();
      }
      return true;
    });
    el.addEventListener("click", function(event) {
      // alert(this.innerHTML);
      // event.preventDefault();
      // event.stopPropagation();
      return true;
    });
  });
    
 </script>
        </div>
    


        </div>
    </div>

















<script>
    var _prum = [['id', '58b7714c7540548d787b23c6'],
        ['mark', 'firstbyte', (new Date()).getTime()]];
    (function() {
        var s = document.getElementsByTagName('script')[0]
                , p = document.createElement('script');
        p.async = 'async';
        p.src = '//rum-static.pingdom.net/prum.min.js';
        s.parentNode.insertBefore(p, s);
    })();
</script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/vaafb692b2aea4879b33c060e79fe94621666317369993" integrity="sha512-0ahDYl866UMhKuYcW078ScMalXqtFJggm7TmlUtp0UlD4eQk0Ixfnm5ykXKvGJNFjLMoortdseTfsRT8oCfgGA==" data-cf-beacon='{"rayId":"77643e30af0796ef","token":"16f03d22e36d4060b9b3e112eb0bf3d7","version":"2022.11.3","si":100}' crossorigin="anonymous"></script>
</body>
</html>

    


"""

from lxml import etree

res = etree.HTML(text)
all_lists = res.xpath('//div[@class="ar-browse-item"]/a')
data = []
for one in all_lists:
    name = one.xpath('.//div/div/span/div/text()')[0]
    link = one.xpath('.//@href')[0]
    url = urljoin('https://www.annualreviews.org/journal/anchem', link)
    name = 'Annual Review of ' + name
    print(name, url)
    data.append(dict(title_name=name, url=url, pic='', issn=''))
save_list(data, 'annualreviews222.csv', ['title_name', 'url', 'pic', 'issn'])