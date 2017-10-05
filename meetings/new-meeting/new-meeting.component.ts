// Angular dependencies
import { Component, OnInit } from '@angular/core';
// Models
import { Person, Entity, Subject,  Meeting, MeetingSubject, MeetingParticipant } from '../../_models/index';
import { MeetingCategory } from '../../_categories/index';
// Internal Services
import { MeetingService } from '../_services/meeting.service';
// External Services
import { UserDataService } from '../../initialization/_services/user-data.service';
import { CategoriesService } from '../../initialization/_services/categories.service';

// Bootstrap service
import { DragulaService } from 'ng2-dragula';

@Component({
  selector: 'new-meeting',
  templateUrl: './new-meeting.component.html',
  styleUrls: [ './new-meeting.component.css' ]
})

export class MeetingFormComponent {

possible_entities: Entity[];
possible_meetingparticipants: Person[];
possible_meetingsubjects: Subject[];
possible_categories: MeetingCategory[];

model = new Meeting;
submitted = false;


constructor(
    private meetingService: MeetingService,
    private userDataService: UserDataService,
    private categoriesService: CategoriesService
) { }

getEntities(): void {
    this.userDataService.getEntitiesByUser()
    .subscribe(entities => this.possible_entities = entities);
}

getMeetingCategories(): void {
    this.categoriesService.getMeetingCategories()
    .then(categories => this.possible_categories = categories);
}

getMeetingParticipants(_id): void {
    console.log('gotten this id', _id);
    this.meetingService.getMeetingParticipants(_id)
    .then(meetingparticipants => this.possible_meetingparticipants = meetingparticipants);
    }

getMeetingSubjects(_id): void {
    console.log('gotten this id', _id);
    this.meetingService.getMeetingSubjects(_id)
    .then(meetingsubjects => this.possible_meetingsubjects = meetingsubjects);
    }

// What to do when the component initiates
ngOnInit(): void {
    // Populate these fields
    this.getEntities();
    this.getMeetingCategories();
    this.model.meetingparticipants = [];
    this.model.meetingsubjects = [];

}
// What to do when entity field is chosen
onChangeEntity(): void {
    // Populate these fields
    this.getMeetingParticipants(this.model.entity.id);
    this.getMeetingSubjects(this.model.entity.id);
}

onSelectPerson(person: Person) {
    // Construct instance of MeetingParticipant from selected item, and add it as participant in the current meeting instance
    let meetingparticipant = new MeetingParticipant;
    meetingparticipant.person = person;
    this.model.meetingparticipants.push(meetingparticipant);
    // Remove the selected instance from list of possible meetingparticipants
    let index: number = this.possible_meetingparticipants.indexOf(person);
    if (index !== -1) {
        this.possible_meetingparticipants.splice(index, 1);
    }
}

onSelectSubject(subject: Subject) {
    // Construct instance of MeetingSubject from selected item, and add it as meeting subject in the current meeting instance
    let meetingsubject = new MeetingSubject;
    meetingsubject.subject = subject;
    // meetingsubject.listposition_on_request = TBA add position.
    this.model.meetingsubjects.push(meetingsubject);
    // Remove the selected instance from list of possible subjects
    let index: number = this.possible_meetingsubjects.indexOf(subject);
    if (index !== -1) {
        this.possible_meetingsubjects.splice(index, 1);
    }
}

onClickRemoveMeetingParticipant(participant) {
    let index: number = this.model.meetingparticipants.indexOf(participant);
    if (index !== -1) {
        this.possible_meetingparticipants.push(participant.person);
        this.model.meetingparticipants.splice(index, 1);
    }
}

onClickRemoveSubject(meetingsubject) {
    let index: number = this.model.meetingsubjects.indexOf(meetingsubject);
    if (index !== -1) {
        this.possible_meetingsubjects.push(meetingsubject.subject);
        this.model.meetingsubjects.splice(index, 1);
    }
}

onSubmit() {
    // Set up a send model, populate this with correct data for POST meeting
    let send_model = {
        meeting_category: null,
        entity: null,
        requested_meetdate: null,
    } ;
    send_model.meeting_category = this.model.meeting_category.id;
    send_model.entity = this.model.entity.id;
    send_model.requested_meetdate = this.model.requested_meetdate;
    console.dir(send_model);

    // Get meeting as return from API, and use this in POST to paricipants and meeting subjects
    let meeting = this.meetingService.createMeeting(send_model).then(res => {
        console.log(res);
       // Loop to set correct data for sending meetingparticipants
        let send_meetingparticipants = [];
        for (let i in this.model.meetingparticipants) {
            if (this.model.meetingparticipants.hasOwnProperty(i)) {
                 console.log(i);
                // tslint:disable-next-line:prefer-const
                let sendparticipant = {
                    is_invited : true,
                    person : this.model.meetingparticipants[i].person.id,
                    meeting : res.id
                };
                send_meetingparticipants.push(sendparticipant);
            }
        }
        // Loop to set correct data for sending meeting subjects
        let send_meetingsubjects = [];
        for (let i in this.model.meetingsubjects) {
            console.log(i);
            let send_meetingsubject = {
                listposition_on_request : parseInt(i),
                listposition_on_report : parseInt(i),
                subject : this.model.meetingsubjects[i].subject.id,
                meeting : res.id
            };
        send_meetingsubjects.push(send_meetingsubject);
        }
        console.dir(send_meetingparticipants);
        console.dir(send_meetingsubjects);
        this.meetingService.createMeetingParticipants(send_meetingparticipants);
        this.meetingService.createMeetingSubjects(send_meetingsubjects);
    });
    this.submitted = true;
}

  // TODO: Remove this when we're done
  get diagnostic() { return JSON.stringify(this.model); }
}