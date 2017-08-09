import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `
    <nav>
      <a routerLink="/dashboard" routerLinkActive="active">Dashboard</a>
      <a routerLink="/meetings" routerLinkActive="active">Meetings</a>
      <a routerLink="/login" routerLinkActive="active">Login</a>    
    </nav>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'Velkommen til Kontrollrommet!';
}