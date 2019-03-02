constructor(private loginService: MainService, private router: Router) { }
authenticate(form: NgForm) {
       // this.spinnerService.show();
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