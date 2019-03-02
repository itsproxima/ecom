import {Injectable} from '@angular/core';
import {Http, Headers, RequestOptions, RequestMethod, Response} from '@angular/http';
import {Router} from '@angular/router';
import {HttpClient, HttpHeaders, HttpErrorResponse} from '@angular/common/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import {GlobalVariable} from 'globals';
import {ResultModel} from '../model/result';

@Injectable()
export class MainService {

	private apiUrl = "https://reqres.in/api/login";
    subscription: any;
    private header = new Headers({'Content-Type': 'application/json'});
    option = new RequestOptions({headers: this.header});


	constructor(private http: Http, private router: Router) {

    }


    validateUser(emailId: string, password: string): Observable<ResultModel> {
    	document.write("i am coming here!");
        let options = {
            headers: new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded')
        };
        let body = `emailId=${emailId}&password=${password}`;
        this.subscription = this.http.post(GlobalVariable.BASE_API_URL + 'vendor/vendor_login', body)
            .map((res: Response) => res.json());
        return this.subscription;
    }

   

}
