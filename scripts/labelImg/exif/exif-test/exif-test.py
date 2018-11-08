

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>garbage/scripts/labelImg/exif-test.py at tts-JP - shimatani/garbage</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="icon" href="http://jp64sv166.daikin.co.jp/gitbucket/assets/common/images/gitbucket.png?20180711162257" type="image/vnd.microsoft.icon" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/google-fonts/css/source-sans-pro.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/bootstrap-3.3.7/css/bootstrap.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/octicons-4.4.0/octicons.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/bootstrap-datetimepicker-4.17.44/css/bootstrap-datetimepicker.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/colorpicker/css/bootstrap-colorpicker.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/google-code-prettify/prettify.css?20180711162257" type="text/css" rel="stylesheet"/>
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/facebox/facebox.css?20180711162257" rel="stylesheet"/>
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/AdminLTE-2.4.2/css/AdminLTE.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/AdminLTE-2.4.2/css/skins/skin-blue-light.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/font-awesome-4.7.0/css/font-awesome.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery-ui/jquery-ui.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery-ui/jquery-ui.structure.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery-ui/jquery-ui.theme.min.css?20180711162257" rel="stylesheet">
    <link href="http://jp64sv166.daikin.co.jp/gitbucket/assets/common/css/gitbucket.css?20180711162257" rel="stylesheet">
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery/jquery-3.2.1.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery-ui/jquery-ui.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/dropzone/dropzone.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/common/js/validation.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/common/js/gitbucket.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/bootstrap-3.3.7/js/bootstrap.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/bootstrap3-typeahead/bootstrap3-typeahead.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/bootstrap-datetimepicker-4.17.44/js/moment.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/bootstrap-datetimepicker-4.17.44/js/bootstrap-datetimepicker.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/colorpicker/js/bootstrap-colorpicker.min.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/google-code-prettify/prettify.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/elastic/jquery.elastic.source.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/facebox/facebox.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery-hotkeys/jquery.hotkeys.js?20180711162257"></script>
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/jquery-textcomplete-1.8.4/jquery.textcomplete.min.js?20180711162257"></script>
    
      <meta name="go-import" content="jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage git http://jp64sv166.daikin.co.jp/gitbucket/git/shimatani/garbage.git" />
    
    <script src="http://jp64sv166.daikin.co.jp/gitbucket/assets/vendors/AdminLTE-2.4.2/js/adminlte.min.js?20180711162257" type="text/javascript"></script>
  </head>
  <body class="skin-blue-light page-load sidebar-mini ">
    <div class="wrapper">
      <header class="main-header">
        <a href="http://jp64sv166.daikin.co.jp/gitbucket/" class="logo">
          <span class="logo-mini"><img src="http://jp64sv166.daikin.co.jp/gitbucket/assets/common/images/gitbucket.svg?20180711162257" alt="GitBucket" /></span>
          <span class="logo-lg"><img src="http://jp64sv166.daikin.co.jp/gitbucket/assets/common/images/gitbucket.svg?20180711162257" alt="GitBucket" />
          <span class="header-title strong">GitBucket</span>
          <span class="header-version">4.20.0</span></span>
        </a>
        <nav class="navbar navbar-static-top" role="navigation">
          <!-- Sidebar toggle button-->
          
            <a href="#" class="sidebar-toggle" data-toggle="push-menu" role="button">
              <span class="sr-only">Toggle navigation</span>
            </a>
          
          <form id="search" action="http://jp64sv166.daikin.co.jp/gitbucket/search" method="GET" class="pc navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" name="query" id="navbar-search-input" class="form-control" placeholder="Search repository"/>
            </div>
          </form>
          <ul class="pc nav navbar-nav">
            
              <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/dashboard/pulls">Pull requests</a></li>
              <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/dashboard/issues">Issues</a></li>
            
            
              
                <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/gist">Snippets</a></li>
              
            
          </ul>
          <div class="navbar-custom-menu">
            <ul class="nav navbar-nav">
              
                <li class="dropdown notifications-menu">
                  <a class="dropdown-toggle menu" data-toggle="dropdown" href="#">
                    <i class="octicon octicon-plus" style="color: black;"></i><span class="caret" style="color: black; vertical-align: middle;"></span>
                  </a>
                  <ul class="dropdown-menu pull-right" style="width: auto;">
                    <li>
                      <ul class="menu">
                        <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/new">New repository</a></li>
                        <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/groups/new">New group</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
                <li class="dropdown notifications-menu">
                  <a class="dropdown-toggle menu" data-toggle="dropdown" href="#" data-toggle="tooltip" data-placement="bottom" title="Signed is as shimatani">
                    <img src="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/_avatar?20181107155053" class="avatar-mini" style="width: 16px; height: 16px;" /><span class="caret" style="color: black; vertical-align: middle;"></span>
                  </a>
                  <ul class="dropdown-menu pull-right" style="width: auto;">
                    <li>
                      <ul class="menu">
                        <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani">Your profile</a></li>
                        <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/_edit">Account settings</a></li>
                        
                        <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/signout">Sign out</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
              
            </ul>
          </div>
        </nav>
      </header>
      
  



<div class="main-sidebar">
  <div class="sidebar">
    <ul class="sidebar-menu">
      
  <li class = "menu-item-hover active">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage">
        <i class="menu-icon octicon octicon-code"></i>
        <span>Files</span>
        
      </a>
    
  </li>

      
        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/branches">
        <i class="menu-icon octicon octicon-git-branch"></i>
        <span>Branches</span>
        
          <span class="pull-right-container"><span class="label label-primary pull-right">2</span></span>
        
      </a>
    
  </li>

        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/tags">
        <i class="menu-icon octicon octicon-tag"></i>
        <span>Tags</span>
        
          <span class="pull-right-container"><span class="label label-primary pull-right">1</span></span>
        
      </a>
    
  </li>

      
      
        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/issues">
        <i class="menu-icon octicon octicon-issue-opened"></i>
        <span>Issues</span>
        
      </a>
    
  </li>

        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/pulls">
        <i class="menu-icon octicon octicon-git-pull-request"></i>
        <span>Pull requests</span>
        
      </a>
    
  </li>

        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/issues/labels">
        <i class="menu-icon octicon octicon-tag"></i>
        <span>Labels</span>
        
      </a>
    
  </li>

        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/issues/priorities">
        <i class="menu-icon octicon octicon-flame"></i>
        <span>Priorities</span>
        
      </a>
    
  </li>

        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/issues/milestones">
        <i class="menu-icon octicon octicon-milestone"></i>
        <span>Milestones</span>
        
      </a>
    
  </li>

      
      
        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/wiki">
        <i class="menu-icon octicon octicon-book"></i>
        <span>Wiki</span>
        
      </a>
    
  </li>

      
      
        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/network/members">
        <i class="menu-icon octicon octicon-repo-forked"></i>
        <span>Forks</span>
        
      </a>
    
  </li>

      
      
        
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/settings">
        <i class="menu-icon octicon octicon-gear"></i>
        <span>Settings</span>
        
      </a>
    
  </li>

      
      
        
          
  <li class = "menu-item-hover ">
    
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/network">
        <i class="menu-icon octicon octicon-circuit-board"></i>
        <span>Network</span>
        
      </a>
    
  </li>

        
      
    </ul>
  </div>
</div>
<div class="content-wrapper">
  <div class="content body clearfix">
    <div class="headbar">
      <div class="container">
        


        

        <div class="head">
          <div class="pull-right">
            
              


  <div class="btn-group" >
    <button id = "test"
        class="dropdown-toggle btn btn-default btn-sm" data-toggle="dropdown">
      
        
        <span class="strong"
              >
          Watching
        </span>
      
      <span class="caret"></span>
    </button>
    <ul class="dropdown-menu pull-right">
      
      
  
    <li>
      <a href="#" class="watch" data-id="watching">
        

  <i class="octicon octicon-check"></i>

        <span class="notification-label strong">Watching</span>
        <div class="muted small">Notify all conversations.</div>
      </a>
    </li>
  
    <li>
      <a href="#" class="watch" data-id="not_watching">
        

  <i class="octicon"></i>

        <span class="notification-label strong">Not watching</span>
        <div class="muted small">Notify when participating.</div>
      </a>
    </li>
  
    <li>
      <a href="#" class="watch" data-id="ignoring">
        

  <i class="octicon"></i>

        <span class="notification-label strong">Ignoring</span>
        <div class="muted small">Never notify.</div>
      </a>
    </li>
  

    </ul>
  </div>
  


<script>
$(function(){
  $('a.watch').click(function(){
    var selected = $(this);
    var notification = selected.data('id');
    $.post('http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/watch',
      { notification : notification },
      function(){
        $('a.watch i.octicon-check').removeClass('octicon-check');
        $('a.watch[data-id=' + notification + '] i').addClass('octicon-check');

        // Update button label
        var label = selected.find('span.notification-label').text().trim();
        selected.parents('div.btn-group').find('button>span.strong').text(label);
      }
    );
    return false;
  });
});
</script>

            
          </div>
          

  
    <i class="mega-octicon octicon-repo"></i>
  


          <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani">shimatani</a> / <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage" class="strong">garbage</a>

          
            
          
        </div>
      </div>
    </div>
    
    <div class="head">
      <div class="pull-right hide-if-blame"><div class="btn-group">
        <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/blob/e9b55325e6c1e102c286e5d141033bc2dc64bbb9/scripts/labelImg/exif-test.py" data-hotkey="y" style="display: none;">Transfer to URL with SHA</a>
        <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/find/tts-JP" class="btn btn-sm btn-default" data-hotkey="t">Find file</a>
      </div></div>
      <div class="line-age-legend">
        <span>Newer</span>
        <ol>
            <li class="heat1"></li>
            <li class="heat2"></li>
            <li class="heat3"></li>
            <li class="heat4"></li>
            <li class="heat5"></li>
            <li class="heat6"></li>
            <li class="heat7"></li>
            <li class="heat8"></li>
            <li class="heat9"></li>
            <li class="heat10"></li>
        </ol>
        <span>Older</span>
      </div>
      <div id="branchCtrlWrapper" style="display:inline;">
      


  <div class="btn-group" >
    <button id = "test"
        class="dropdown-toggle btn btn-default btn-sm" data-toggle="dropdown">
      
        
          <span class="muted">branch:</span>
        
        <span class="strong"
              style="display:inline-block; vertical-align:bottom; overflow-x:hidden; max-width:200px; text-overflow:ellipsis">
          tts-JP
        </span>
      
      <span class="caret"></span>
    </button>
    <ul class="dropdown-menu">
      
      
  <li><div id="branch-control-title">Switch branches<button id="branch-control-close" class="pull-right">&times</button></div></li>
  <li><input id="branch-control-input" type="text" class="form-control input-sm dropdown-filter-input" placeholder="Find or create branch ..."/></li>
  
        
          <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/blob/master/scripts/labelImg/exif-test.py">

  <i class="octicon"></i>
 master</a></li>
        
          <li><a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/blob/tts-JP/scripts/labelImg/exif-test.py">

  <i class="octicon octicon-check"></i>
 tts-JP</a></li>
        
      
  
    <li id="create-branch" style="display: none;">
      <a><form action="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/branches" method="post" style="margin: 0;">
        <span class="strong">Create branch:&nbsp;<span class="new-branch"></span></span>
        <br><span style="padding-left: 17px;">from&nbsp;'tts-JP'</span>
        <input type="hidden" name="new">
        <input type="hidden" name="from" value="tts-JP">
      </form></a>
    </li>
  

    </ul>
  </div>
  


<script>
  $(function(){
    $('#branch-control-input').parent().click(function(e) {
      e.stopPropagation();
    });
    $('#branch-control-close').click(function() {
      $('[data-toggle="dropdown"]').parent().removeClass('open');
    });
    $('#branch-control-input').keyup(function() {
      var inputVal = $('#branch-control-input').val();
      $.each($('#branch-control-input').parent().parent().find('a'), function(index, elem) {
        if (!inputVal || !elem.text.trim() || elem.text.trim().toLowerCase().indexOf(inputVal.toLowerCase()) >= 0) {
          $(elem).parent().show();
        } else {
          $(elem).parent().hide();
        }
      });
      
        if (inputVal) {
          $('#create-branch').parent().find('li:last-child').show().find('.new-branch').text(inputVal);
        } else {
          $('#create-branch').parent().find('li:last-child').hide();
        }
      
    });
    
      $('#create-branch').click(function() {
        $(this).find('input[name="new"]').val($('.dropdown-menu input').val())
        $(this).find('form').submit()
       });
    
    $('.btn-group').click(function() {
      $('#branch-control-input').val('');
      $('.dropdown-menu li').show();
      $('#create-branch').hide();
    });
  });
</script>

      </div>
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/tree/tts-JP">garbage</a> /
      
        
          <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/tree/tts-JP/scripts">scripts</a> /
        
      
        
          <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/tree/tts-JP/scripts/labelImg">labelImg</a> /
        
      
        
          exif-test.py
        
      
      
    </div>
    <div class="box-header">
      <img src="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/_avatar?20181107155053" class="avatar" style="width: 28px; height: 28px;" />
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani" class="username strong">shimatani</a>
      <span class="muted">
<span data-toggle="tooltip" title="2018-10-16 13:00:26">
  
    22 days ago
  
</span>
</span>
      <span class="label label-default">2 KB</span>
      <a href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/commit/e9b55325e6c1e102c286e5d141033bc2dc64bbb9" class="commit-message">PILとOpenCVにおけるExif情報の取り扱いをテストする</a>
      <div class="btn-group pull-right">
        
          <a class="btn btn-sm btn-default" href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/edit/tts-JP/scripts/labelImg/exif-test.py">Edit</a>
        
        <a class="btn btn-sm btn-default" href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/raw/e9b55325e6c1e102c286e5d141033bc2dc64bbb9/scripts/labelImg/exif-test.py">Raw</a>
        
          <a class="btn btn-sm btn-default blame-action" href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/blame/e9b55325e6c1e102c286e5d141033bc2dc64bbb9/scripts/labelImg/exif-test.py"
            data-url="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/get-blame/e9b55325e6c1e102c286e5d141033bc2dc64bbb9/scripts/labelImg/exif-test.py" data-repository="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage">Blame</a>
        
        <a class="btn btn-sm btn-default" href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/commits/tts-JP/scripts/labelImg/exif-test.py">History</a>
        
          <a class="btn btn-sm btn-danger" href="http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/remove/tts-JP/scripts/labelImg/exif-test.py">Delete</a>
        
      </div>
    </div>
      
        
          
            <div class="box-content-bottom">
              <pre class="prettyprint linenums blob  no-renderable  ">#! -*- coding: utf-8 -*-
import sys
import os
from PIL import Image
import cv2
import numpy as np

# メイン
def main():
    # 引数１から画像ファイル名取得
    args = sys.argv
    if (len(args) != 2):
        print(&quot;Usage: $ python &quot; + args[0] + &quot; sample.jpg&quot;)
        quit()

    file_path = args[1]
    print(&quot;File path (args[1]) is %s&quot; % file_path)

    ############################
    # PIL による open～save
    ############################
    img = Image.open(file_path)
    # img.show()

    # Exif 取得。存在しない場合、空の辞書を返して終了する
    exif = img._getexif()

    # 画像の向き取得
    try:
        orientation = exif.get(0x112, 1)
        print(&#x27; Orientation: {0}&#x27;.format(orientation))
    except AttributeError:
        print(&quot; img の Exif の Orientation が存在しません&quot;)
        return {}

    # 回転しないで保存する新しいファイル名の準備
    ftitle, fext = os.path.splitext(file_path)

    # &lt;1&gt;
    # Exif なしでファイル保存
    # Exif 情報を反映するフォトビューアーと同じ画像を保存
    # Exif の向き情報（Orientation）なし
    new_file_path = ftitle + &#x27;-orient-&#x27; + str(orientation) + &#x27;_PIL&#x27; + fext

    # print(&quot;New File path is %s&quot; % new_file_path)
    img.save(new_file_path, &#x27;JPEG&#x27;)
    print(&quot;&lt;1&gt; %s を保存しました&quot; % new_file_path)

    # &lt;2&gt;
    # Exif つきでファイル保存
    # Exif 情報を反映しない Chrome と同じ画像を保存
    # Exif の向き情報（Orientation）あり
    exif = img.info[&#x27;exif&#x27;]
    new_file_path = ftitle + &#x27;-orient-&#x27; + str(orientation) + &#x27;_PIL+Exif&#x27; + fext
    img.save(new_file_path, &#x27;JPEG&#x27;, exif=exif)
    print(&quot;&lt;2&gt; %s を保存しました&quot; % new_file_path)

    ############################
    # OpenCV による open～save
    ############################
    # &lt;3&gt;
    # Exif 無視でオープン
    # Exif 情報を反映するフォトビューアーと同じ向きでオープン
    img = cv2.imread(file_path, cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)
    cv2.imshow(file_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存
    # Exif の向き情報（Orientation）なし
    new_file_path = ftitle + &#x27;-orient-&#x27; + str(orientation) + &#x27;_CV2&#x27; + fext
    cv2.imwrite(new_file_path ,img)
    print(&quot;&lt;3&gt; %s を保存しました&quot; % new_file_path)

    # &lt;4&gt;
    # Exif 反映してオープン
    # Exif 情報を反映しない Chrome と同じ向きでオープン
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    cv2.imshow(file_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存
    # Exif の向き情報（Orientation）なし
    new_file_path = ftitle + &#x27;-orient-&#x27; + str(orientation) + &#x27;_CV2+Exif&#x27; + fext
    cv2.imwrite(new_file_path ,img)
    print(&quot;&lt;4&gt; %s を保存しました&quot; % new_file_path)

if __name__ == &#x27;__main__&#x27;:
	main()

print(&quot;Done!&quot;)
</pre>
            </div>
          
        
      
      
      
  
  </div>
</div>



    </div>
    <script>
      $(function(){
        $('#search').submit(function(){
          return $.trim($(this).find('input[name=query]').val()) != '';
        });
        
          $(".sidebar-toggle").on('click', function(e){
            $.post('http://jp64sv166.daikin.co.jp/gitbucket/sidebar-collapse', { collapse: !$('body').hasClass('sidebar-collapse') });
          });
        
      });
    </script>
    
  </body>
</html>

<script>
$(window).on('load', function(){
  updateHighlighting();

  window.onhashchange = function(){
    updateHighlighting();
  }

  var pre = $('pre.prettyprint');
  function updateSourceLineNum(){
    $('.source-line-num').remove();
    var pos = pre.find('ol.linenums').position();
    if(pos){
      $('<div class="source-line-num">').css({
        height  : pre.height(),
        width   : '48px',
        cursor  : 'pointer',
        position: 'absolute',
        top     : pos.top + 'px',
        left    : pos.left + 'px'
      }).click(function(e){
        var pos = $(this).data("pos");
        if(!pos){
          pos = $('ol.linenums li').map(function(){ return { id: $(this).attr("id"), top: $(this).position().top} }).toArray();
          $(this).data("pos",pos);
        }
        for(var i = 0; i < pos.length-1; i++){
          if(pos[i + 1].top > e.pageY){
            break;
          }
        }
        var line = pos[i].id.replace(/^L/,'');
        var hash = location.hash;
        var commitUrl = 'http://jp64sv166.daikin.co.jp/gitbucket/shimatani/garbage/blob/e9b55325e6c1e102c286e5d141033bc2dc64bbb9/scripts/labelImg/exif-test.py';
        if(e.shiftKey == true && hash.match(/#L\d+(-L\d+)?/)){
          var lines = hash.split('-');
          window.history.pushState('', '', commitUrl + lines[0] + '-L' + line);
        } else {
          var p = $("#L"+line).attr('id',"");
          window.history.pushState('', '', commitUrl + '#L' + line);
          p.attr('id','L'+line);
        }
        $("#branchCtrlWrapper .btn .muted").text("tree:");
        $("#branchCtrlWrapper .btn .strong").text("e9b55325e6");
        updateHighlighting();
      }).appendTo(pre);
    }
  }
  var repository = $('.blame-action').data('repository');
  $('.blame-action').click(function(e){
    if(history.pushState && $('pre.prettyprint.no-renderable').length){
      e.preventDefault();
      history.pushState(null, null, this.href);
      updateBlame();
    }
  });

  function updateBlame(){
    var m = /\/(blame|blob)(\/.*)$/.exec(location.href);
    var mode = m[1];
    $('.blame-action').toggleClass("active", mode=='blame').attr('href', repository + (m[1] == 'blame' ? '/blob' : '/blame') + m[2]);
    if(pre.parents("div.box-content-bottom").find(".blame").length){
      pre.parent().toggleClass("blame-container", mode == 'blame');
      updateSourceLineNum();
      return;
    }
    if(mode=='blob'){
      updateSourceLineNum();
      return;
    }
    $(document.body).toggleClass('no-box-shadow', document.body.style.boxShadow === undefined);
    $('.blame-action').addClass("active");
    var base = $('<div class="blame">').css({height: pre.height()}).prependTo(pre.parents("div.box-content-bottom"));
    base.parent().addClass("blame-container");
    updateSourceLineNum();
    $.get($('.blame-action').data('url')).done(function(data){
      var blame = data.blame;
      var index = [];
      for(var i = 0; i < blame.length; i++){
        for(var j = 0; j < blame[i].lines.length; j++){
          index[blame[i].lines[j]] = blame[i];
        }
      }
      var blame, lastDiv, now = new Date().getTime();

      $('pre.prettyprint ol.linenums li').each(function(i, e){
        var p = $(e).position();
        var h = $(e).height();
        if(blame == index[i]){
          lastDiv.css("min-height",(p.top + h + 1) - lastDiv.position().top);
        } else {
          $(e).addClass('blame-sep')
          blame = index[i];
          var sha = $('<div class="blame-sha">')
             .append($('<a>').attr("href", data.root + '/commit/' + blame.id).text(blame.id.substr(0,7)));
          if(blame.prev){
             sha.append($('<br />'))
             .append($('<a class="muted-link">').text('prev').attr("href", data.root + '/blame/' + blame.prev + '/' + (blame.prevPath || data.path)));
          }
          lastDiv = $('<div class="blame-info">')
           .addClass('heat' + Math.min(10, Math.max(1, Math.ceil((now - blame.commited) / (24 * 3600 * 1000 * 70)))))
           .toggleClass('blame-last', blame.id == data.last)
           .data('line', (i + 1))
           .css({
             "top"        : p.top + 'px',
             "min-height" : h + 'px'
           })
           .append(sha)
           .append($(blame.avatar).addClass('avatar').css({"float": "left"}))
           .append($('<div class="blame-commit-title">').text(blame.message))
           .append($('<div class="muted">').html(blame.author + " authed " + blame.authed))
           .appendTo(base);
        }
      });
    });
    return false;
  };
  updateBlame();
});

var scrolling = false;

/**
 * Hightlight lines which are specified by URL hash.
 */
function updateHighlighting(){
  var hash = location.hash;
  if(hash.match(/#L\d+(-L\d+)?/)){
    $('li.highlight').removeClass('highlight');
    var lines = hash.substr(1).split('-');
    if(lines.length == 1){
      $('#' + lines[0]).addClass('highlight');
      if(!scrolling){
        $(window).scrollTop($('#' + lines[0]).offset().top - 40);
      }
    } else if(lines.length > 1){
      var start = parseInt(lines[0].substr(1));
      var end   = parseInt(lines[1].substr(1));
      for(var i = start; i <= end; i++){
        $('#L' + i).addClass('highlight');
      }
      if(!scrolling){
        $(window).scrollTop($('#L' + start).offset().top - 40);
      }
    }
    scrolling = true;
  }
}
</script>
