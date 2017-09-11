﻿import { Component, OnInit } from '@angular/core';

//Models
import { User } from '../../_models/index';

// Internal Services
import { UserService } from '../index';

@Component({
    moduleId: module.id,
    templateUrl: 'users.component.html'
})

export class UsersComponent implements OnInit {
    currentUser: User;
    users: User[] = [];

    constructor(private userService: UserService) {
        this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
    }

    ngOnInit() {
        this.loadAllUsers();
    }

    deleteUser(id: number) {
        this.userService.delete(id).subscribe(() => { this.loadAllUsers() });
    }

    private loadAllUsers() {
        this.userService.getAll().subscribe(users => { this.users = users; });
    }
}