//***Angular modules***
import { NgModule }       from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }    from '@angular/forms';
import { HttpModule }    from '@angular/http';

// ***Foreign Modules***
// Bootstrap UI 
import { SortableModule } from 'ngx-bootstrap';
import { DragulaModule } from 'ng2-dragula'

// *** Other Modules ***
import { AppRoutingModule } from '../router.module';

// *** Application Elements
//meetings
import { MeetingsComponent }  from './index';
import { MeetingListComponent } from "./index";
import { MeetingFormComponent } from './index';

// Services
import { MeetingService } from './_services/meeting.service';

@NgModule({
  imports: [ // Necessary Modules
  // Angular dependent modules
    CommonModule,
    FormsModule,
    HttpModule,
  // Sortable module from Bootstrap
    SortableModule.forRoot(),
  // Dragula module from Bootstrap
    DragulaModule,
  //The Routing module
    AppRoutingModule,
  ],
  declarations: [ // Components and Directives
    MeetingsComponent,
    MeetingListComponent,
    MeetingFormComponent
  ],
  providers: [ // Services
    // Application services
    MeetingService,
  ],
  exports: [
    MeetingListComponent
  ] 
})
export class MeetingsModule { }