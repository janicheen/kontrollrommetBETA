import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

import { DataService } from '../_services/data.service';

@Injectable()
export class AuthGuard implements CanActivate {

    constructor(
        private dataService: DataService,
        private router: Router
    ) { }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        if (this.dataService.isloggedIn()) {
            // logged in is returned true
            console.log('canActivate says I am logged in');
            return true;
        } else {
            console.log('canActivate says I am NOT logged in');
            // not logged in so redirect to login page with the return url
            this.router.navigate(['/login'], { queryParams: { returnUrl: state.url }});
        return false;
        }
    }
}