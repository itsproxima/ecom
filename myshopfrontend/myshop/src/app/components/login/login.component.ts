import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import {Router} from '@angular/router';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {ResultModel} from '../../model/result';
import {UserModel} from '../../model/userDetails';
import {MainserviceService} from '../../service/mainservice.service';
//import {Ng4LoadingSpinnerService} from 'ng4-loading-spinner';
//import {SweetAlertService} from 'angular-sweetalert-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
	emailId: string;
    password: string;
   userModel: UserModel;
   resultModel: ResultModel;
   /*private loginService: MainService;
   private router: Router)*/
    
   router: Router;

  constructor(private loginService:MainserviceService ) { }

  ngOnInit() {
  }

 /* authenticate(form: NgForm) {
       // this.spinnerService.show();
       document.write("Hello World!");

        this.loginService.validateUser(this.emailId, this.password)
            .subscribe(res => {
                    //this.spinnerService.hide();
		                    console.log("res:" + JSON.stringify(res));
		                    this.resultModel = res;
		                    

		                    if (this.resultModel.code == '01') {
		                    }


		                    else {
		                        this.userModel = this.resultModel.data;
		                        localStorage.setItem("user", JSON.stringify(this.userModel));
		                        this.router.navigate(['/dashboard']);
		                    }
                },
                (err: HttpErrorResponse) => {
                    //this.spinnerService.hide();
                    if (err.error instanceof Error) {
                    }
                    else {
                    }
                }
            );
    }
    */
   authenticate(form: NgForm) {
   
    //console.log("hello i am in login component");
    this.loginService.validateUser(this.emailId, this.password).subscribe(res=>{
        console.log(JSON.stringify(res))
    })
   }
}
