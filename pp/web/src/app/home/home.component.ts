import { FormBuilder, FormGroup } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { User } from '@/_models';
import { UserService, AuthenticationService } from '@/_services';

@Component({ templateUrl: 'home.component.html' })
export class HomeComponent implements OnInit {
    currentUser: User;
    users: any = [];
    filterForm: FormGroup;
    loading = false;
    submitted = false;
    name = '';
    username = '';
    
    public itemsPerPage: number;
    public totalItens: number;
    public currentPage: number;
    public maxPagLinks: number;

    constructor(
        private formBuilder: FormBuilder,
        private authenticationService: AuthenticationService,
        private userService: UserService
    ) {
        // this.currentUser = this.authenticationService.currentUserValue;
    }

    ngOnInit() {
        this.filterForm = this.formBuilder.group({
            name: [''],
            username: ['']
        });
        
        this.itemsPerPage = 15;
        this.maxPagLinks = 10;
        this.currentPage = 1;
        this.totalItens = 8078159;

        this.loadAllUsers(this.currentPage - 1, null, null);
    }

    private loadAllUsers(start, name, username) {
        this.userService.getAll(start, name, username)
            .pipe(first())
            .subscribe(data => {
                this.users = data.users;
                this.totalItens = data.total;
                this.loading = false;
            });
    }
    
    onSubmit() {
        this.submitted = true;
        this.loading = true;
        
        this.name = this.filterForm.value.name;
        this.username = this.filterForm.value.username;
        
        this.currentPage = 1;
        
        this.loadAllUsers(this.currentPage - 1, this.name, this.username);
    }
    
    public changePage(event: any): void {
        // Altera a página quando clicado no link
        this.currentPage = event.page;
        // sempre que o usuario trocar a pagina, pegamos a nova pagina dos dados
        this.loadAllUsers(this.currentPage - 1, this.name, this.username);
    }
}