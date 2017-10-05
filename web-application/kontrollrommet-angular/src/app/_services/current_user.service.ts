// Angular dependencies
import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
// rxjs Dependencies
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
// Angular2 JWT dependencies
import { AuthHttp } from 'ng-jwt';
// Models
import { User } from '../_models/index';
import { Entity, Meeting, MeetingParticipant } from '../_models/index';

@Injectable()
export class CurrentUserService {
    private headers = new Headers({'Accept': 'application/json', 'Content-Type': 'application/json'});
    private options = new RequestOptions({ headers: this.headers });

    constructor(
        private authHttp: AuthHttp,
        private http: Http
    ) { }

    createUser(user) {
        console.log('creating user', JSON.stringify({ user }));
        return this.http.post('http://127.0.0.1:8000/client_views/createuser/', JSON.stringify(user), this.options)
        .map(res => res.json()) // ...and calling .json() on the response to return data
        .catch((error: any) => Observable.throw(error.json().error || 'Server error')) // ...errors if
        .subscribe();
    }

    // Method for getting data on currently logged in user
    getCurrentUser(): Observable<User> {
        console.log('getting current user from server...');
        return this.authHttp.get('http://127.0.0.1:8000/client_views/currentuser/')
        .map(res => res.json())
        .catch((error: any) => Observable.throw(error.json().error || 'Server error')); // ...errors if
    }

    getMeetingParticipantByUser(): Observable<MeetingParticipant[]> {
        console.log('getting meetings related to user from server...');
        return this.authHttp.get('http://127.0.0.1:8000/client_views/meetingparticipantbyuser/')
        .map(res => res.json())
        .catch((error: any) => Observable.throw(error.json().error || 'Server error')); // ...errors if
    }
/*     // private helper methods
    private handleError(error: any): Promise<any> {
        console.error('This is the error handler speaking:', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }
 */
}