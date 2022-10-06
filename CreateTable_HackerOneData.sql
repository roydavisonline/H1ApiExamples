USE [HackerOneData]
GO

/****** Object:  Table [dbo].[Reports]    Script Date: 10/6/2022 1:15:20 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Reports](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[reportId] [nvarchar](50) NOT NULL,
	[reportState] [nvarchar](50) NULL,
	[reportCreatedDateTime] [datetime] NULL,
	[reportTitle] [nvarchar](150) NULL,
	[reportTriagedDateTime] [datetime] NULL,
	[reportClosedDateTime] [datetime] NULL,
	[reportLastReporterActivityDateTime] [datetime] NULL,
	[reportFirstProgramActivityDateTime] [datetime] NULL,
	[reportLastProgramActivityDateTime] [datetime] NULL,
	[reportBountyAwardedDateTime] [datetime] NULL,
	[reportBountyAwardedAmount] [money] NULL,
	[reportSwagAwardedDateTime] [datetime] NULL,
	[reportDisclosedDateTime] [datetime] NULL,
	[reportLastPublicActivityDateTime] [datetime] NULL,
	[reportLastActivityDateTime] [datetime] NULL,
	[reportIssueTrackerUrl] [nvarchar](150) NULL,
	[researcherUsername] [nvarchar](512) NULL,
	[researcherName] [nvarchar](512) NULL,
	[researcherReputation] [nvarchar](10) NULL,
	[researcherSignal] [nvarchar](10) NULL,
	[researcherImpact] [nvarchar](10) NULL,
	[reportSeverityCVSSRating] [nvarchar](50) NULL,
	[reportSeverityCVSSScore] [nvarchar](10) NULL,
	[reportSeverityCVSSSComplexity] [nvarchar](10) NULL,
	[reportSeverityCVSSSVector] [nvarchar](10) NULL,
	[reportSeverityCVSSSAvailability] [nvarchar](10) NULL,
	[reportSeverityCVSSConfidentiality] [nvarchar](10) NULL,
	[reportSeverityCVSSIntegrity] [nvarchar](10) NULL,
	[reportSeverityCVSSPrivileges] [nvarchar](10) NULL,
	[reportSeverityCVSSUserInteraction] [nvarchar](10) NULL,
	[reportSeverityCVSSScopeChange] [nvarchar](10) NULL,
	[reportWeaknessName] [nvarchar](150) NULL,
	[reportWeaknessCWEID] [nvarchar](50) NULL,
	[reportScopeAssetType] [nvarchar](50) NULL,
	[reportScopeAssetIdentifier] [nvarchar](50) NULL,
	[bbProgramId] [nvarchar](50) NULL,
	[reportCustomFieldSubTakeover] [nvarchar](50) NULL,
	[reportCustomFieldIPaddress] [nvarchar](50) NULL,
	[ipAddressCountry] [nvarchar](50) NULL,
	[ipAddressCountryCode] [nvarchar](50) NULL,
	[ipAddressCity] [nvarchar](50) NULL,
	[ipAddressRegion] [nvarchar](50) NULL,
	[ipAddressPostalCode] [nvarchar](50) NULL,
	[ipAddressLatitude] [nvarchar](50) NULL,
	[ipAddressLongitude] [nvarchar](50) NULL,
	[reportVulnerabilityInformation] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


