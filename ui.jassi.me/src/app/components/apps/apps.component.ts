import { AfterViewInit, Component, OnDestroy, OnInit } from '@angular/core';
import initAOS, { cleanAOS } from '../../library/invokers/animate-on-scroll';
import { NgFor } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-apps',
  standalone: true,
  imports: [NgFor,RouterModule],
  templateUrl: './apps.component.html',
  styleUrl: './apps.component.css'
})
export class AppsComponent implements AfterViewInit,OnInit,OnDestroy {
  ngAfterViewInit(): void {
		initAOS();
	}
	ngOnDestroy(): void {
		cleanAOS();
	}
	ngOnInit(): void {
		
	}

	cardData = [
		{
			Title: 'Css Formatter',
			Description: 'Lightroom presets crafted for yall',
			Logo: './assets/images/artifacts/photography.svg',
			Aos:'flip-up',
			Duration:'300'
		},
    {
			Title: 'HTML Formatter',
			Description: 'Music production sample packs',
			Logo: './assets/images/artifacts/music.svg',
			Aos:'flip-down',
			Duration:'600'
		}
	];

  cardData2 = [
		{
			Title: 'JS Formatter',
			Description: 'Music production sample packs',
			Logo: './assets/images/artifacts/music.svg',
			Aos:'flip-down',
			Duration:'600'
		},
    {
			Title: 'Hashtag Finder',
			Description: 'Music production sample packs',
			Logo: './assets/images/artifacts/music.svg',
			Aos:'flip-down',
			Duration:'600'
		}
	];

}
