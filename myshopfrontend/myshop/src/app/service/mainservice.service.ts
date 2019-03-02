import { Injectable } from '@angular/core';
import {Http, Headers, RequestOptions, RequestMethod, Response} from '@angular/http';
import {Router} from '@angular/router';
import {HttpClient, HttpHeaders, HttpErrorResponse} from '@angular/common/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import {GlobalVariable} from 'globals';
import {ResultModel} from '../model/result';
import {DataModel} from '../model/data';

/*
@Injectable()
export class MainserviceService {

	private apiUrl = "https://reqres.in/api/";
    subscription: any;
    text:any;
    private header = new Headers({'Content-Type': 'application/json'});
    option = new RequestOptions({headers: this.header});

  constructor(private http: Http, private router: Router) { }

  validateUser(emailId: string, password: string): Observable<ResultModel> {

  		
        let options = {
            headers: new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded')
        };
        let body = `emailId=${emailId}&password=${password}`;
        this.subscription = this.http.post(GlobalVariable.BASE_API_URL + 'vendor/vendor_login', body)
            .map((res: Response) => res.json());
        return this.subscription;
    }

   getproducts(): Observable<ResultModel> {

  		
        let options = {
            headers: new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded')
        };
        let body = ``;
        this.subscription = this.http.get(GlobalVariable.BASE_API_URL + 'users?page=2', body)
            .map((res: Response) => res.json());
        return this.subscription;
    }



}
*/

@Injectable()
export class MainserviceService {

	private apiUrl:string= "/../../assets/data/products.json";
   
  constructor(private http: Http, private router: Router) { }

  
   getCategories():Observable<ResultModel>{
console.log("hello ");

  		return this.http.get('http://bloomsmobility.com/saatvika/api/vendor/categoryall').map((res:Response)=>res.json());
       
    }

    validateUser(emailId: string, password: string): Observable<ResultModel> {

        return this.http.get('http://bloomsmobility.com/saatvika/api/vendor/categoryall').map((res:Response)=>res.json());
    }



}
