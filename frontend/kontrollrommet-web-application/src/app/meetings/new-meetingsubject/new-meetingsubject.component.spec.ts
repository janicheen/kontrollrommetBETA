import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewMeetingsubjectComponent } from './new-meetingsubject.component';

describe('NewMeetingsubjectComponent', () => {
  let component: NewMeetingsubjectComponent;
  let fixture: ComponentFixture<NewMeetingsubjectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewMeetingsubjectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewMeetingsubjectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
