Tryhackme En-pass를 보면 다음과 같은 코드가 나온다 
이 부분에 대해서 간략히 분석해보면, 일단 우리의 입력값($title)에 alphanumeric characters이 들어가면 
안 된다는 것을 알 수 있다. 우리의 입력값은 9개여야하고 첫 인자는 2개의 길이 마지막 인자는 3개의 길이를
가져야 한다. 그리고 6번째가 마지막과 값이 다르고 4번째가 8번째 것과 값이 달라야 하며 
각 입력값을 bool 연산을 해서 합쳤을 때 9가 나오면 된다. 

<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
   $title = $_POST["title"];
   if (!preg_match('/[a-zA-Z0-9]/i' , $title )){
          $val = explode(",",$title);
          $sum = 0;
          for($i = 0 ; $i < 9; $i++){
                if ( (strlen($val[0]) == 2) and (strlen($val[8]) ==  3 ))  {
                    if ( $val[5] !=$val[8]  and $val[3]!=$val[7] ) 
                        $sum = $sum+ (bool)$val[$i]."<br>"; 
                }
          }

          if ( ($sum) == 9 ){
              echo $result;//do not worry you'll get what you need.
              echo " Congo You Got It !! Nice ";
            }
                    else{
                      echo "  Try Try!!";
                    }
          }
          else{
            echo "  Try Again!! ";
          }     
  }

$title = ##,!,!,??,!,#,!,#,(((
$title = ##,!,??,#,$,^,&,*,###
$title = $$,!,@,#,$,^,&,*,###
$title = ##,@,!,##,!,??,!,?,(((
$title = ##,?,??,#,$,^,&,*,###
$title = ##,!,??,#,$,??,&,*,)))
