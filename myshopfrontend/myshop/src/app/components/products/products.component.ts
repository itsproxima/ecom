import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import {Router} from '@angular/router';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {ResultModel} from '../../model/result';
import {DataModel} from '../../model/data';
import {UserModel} from '../../model/userDetails';
import {MainserviceService} from '../../service/mainservice.service';
import { JsonPipe } from '@angular/common';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
	allproducts:any;
	products:any;
  constructor(private productdata:MainserviceService) {}

  ngOnInit() {}
  

  showcategories(){
this.productdata.getCategories().subscribe(res=>{
	console.log(JSON.stringify(res))
})
	}

}
