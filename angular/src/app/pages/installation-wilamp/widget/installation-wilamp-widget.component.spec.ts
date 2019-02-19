import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InstallationWilampWidgetComponent } from './installation-wilamp-widget.component';

describe('DetailComponent', () => {
  let component: InstallationWilampWidgetComponent;
  let fixture: ComponentFixture<InstallationWilampWidgetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InstallationWilampWidgetComponent ],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InstallationWilampWidgetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
