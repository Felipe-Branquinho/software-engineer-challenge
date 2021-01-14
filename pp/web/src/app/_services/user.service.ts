import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { User } from '@/_models';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient) { }
    
    totalItems(): Observable<any> {
        return this.http.get<String>(`${config.apiUrl}/users/total`);
    }

    getAll(start, name, username): Observable<any> {
        return this.http.get<String>(`${config.apiUrl}/users?start=${start}${name ? '&name=' + name : ''}${username ? '&username=' + username : ''}`);
    }

    register(user: any) {
        return this.http.post(`${config.apiUrl}/register`, user);
    }
}