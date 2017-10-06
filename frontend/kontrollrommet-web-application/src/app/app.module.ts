// *** This is the main module, connecting all other sub modules ***

// Angular modules
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
// Angular JWT
import { NgJwtModule } from 'ng-jwt';
// Bootstrap Module
// import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
// Routing Module ***
import { AppRoutingModule } from './app-routing.module';

// App Store
import { AppStore } from './app-store';

// Application Components
import { AppComponent } from './app.component';
import { LoginComponent } from './authentication/login/login.component';
import { RegisterComponent } from './authentication/register/register.component';
import { NavigationFrameComponent } from './navigationframe/navigationframe.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MeetingsComponent } from './meetings/meetings/meetings.component';
import { MeetingListComponent } from './meetings/meeting-list/meeting-list.component';

// Services
import { AuthenticationService, Auth } from 'ng-jwt';
import { AuthService } from './_services/auth.service';
import { AuthGuard } from './_services/auth.guard';
import { HttpService } from './_services/http.service';
import { DataService } from './_services/data.service';
import { MeetingService } from './meetings/meeting.service';

// *** UNSTRUCTURED ***
// import { HttpClientModule, HttpRequest, HTTP_INTERCEPTORS } from '@angular/common/http';
// import { AuthenticationModule } from './authentication/authentication.module';
// import { MainUIModule } from './main-ui/main-ui.module';
// import { MeetingsModule } from './meetings/meetings.module';
// Services
// import { UserDataService } from './initialization/_services/user-data.service';
// import { CategoriesService } from './initialization/_services/categories.service';
// import { MyInterceptorService } from './_services/my-interceptor.service';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LoginComponent,
    NavigationFrameComponent,
    DashboardComponent,
    MeetingsComponent,
    MeetingListComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    NgJwtModule.forRoot({
      loginEndPoint: 'http://127.0.0.1:8000/api-token-auth/',
      headerPrefix: 'JWT',
      loginTokenName: 'token'
    }),
    AppRoutingModule,
   // NgbModule.forRoot(),
    // AuthenticationModule,
    // MainUIModule,
    // MeetingsModule
  ],
  providers: [
    // Apptore
    AppStore,
    // JWT services
    AuthenticationService, Auth,
    // Authentication service
    AuthService,
    AuthGuard,
    // Data service
    DataService,
    // Client views
    HttpService,
    MeetingService
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }